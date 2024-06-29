from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import crud, schemas
from datetime import datetime, timezone, timedelta
import time
import requests
from app.database import get_db

POLYGON_API_KEY = "bs1n5Vdqoi_NOvmCZ_85rrcvtFnYN3vm"
POLYGON_BASE_URL = "https://api.polygon.io/v1/open-close"

stocks_router = APIRouter(prefix='/stock', tags=['stock'])

@stocks_router.get("/{symbol}", response_model=schemas.CreateStock)
async def read_stock(symbol: str, request: Request, db: Session = Depends(get_db)):
    start_time = time.time()
    db_stock = crud.get_stock_by_symbol(db, symbol=symbol)
    
    if db_stock is None or db_stock.from_ != (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'):
        stock_data = fetch_stock_from_polygon(symbol)
        db_stock = crud.create_stock(db, stock_data)

    response_status = 200
    await log_event(db, request, response_status, time.time() - start_time)
    return db_stock


@stocks_router.post("/{symbol}", response_model=dict)
async def update_stock(symbol: str, amount: schemas.AmountUpdateBase, request: Request, db: Session = Depends(get_db)):
    start_time = time.time()
    order = schemas.OrderBase(stock_symbol=symbol, amount=amount.amount)
    crud.update_stock_amount(db, symbol=symbol, amount=order.amount)
    crud.create_order(db, order)
    response_status = 201
    await log_event(db, request, response_status, time.time() - start_time)
    return {"message": f"{amount.amount} units of stock {symbol} were added to your stock record"}

async def log_event(db: Session, request: Request, response_status: int, response_time: float):
    event = schemas.EventBase(
        endpoint=str(request.url),
        method=request.method,
        status_code=response_status,
        response_time=response_time
    )
    crud.create_event(db, event)

def fetch_stock_from_polygon(symbol: str) -> schemas.StockBase:
    yesterday_date = (datetime.now(timezone.utc) - timedelta(days=1)).strftime('%Y-%m-%d')
    #today_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    url = f"{POLYGON_BASE_URL}/{symbol}/{yesterday_date}?apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch stock data")

    data = response.json()
    if data["status"] != "OK":
        raise HTTPException(status_code=404, detail="Stock data not available")

    return schemas.StockBase(
        afterHours=data["afterHours"],
        close=data["close"],
        from_=data["from"],
        high=data["high"],
        low=data["low"],
        open=data["open"],
        preMarket=data["preMarket"],
        status=data["status"],
        symbol=data["symbol"],
        volume=data["volume"],
        performance={},
        amount=0
    )