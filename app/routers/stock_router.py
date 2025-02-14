from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import crud
from datetime import datetime, timezone, timedelta
import time
import requests
from app.database import get_db
from app.schemas import StockBase, EventBase, OrderBase, AmountUpdateBase, CreateStock
from app.routers import constants

stocks_router = APIRouter(prefix='/stock', tags=['stock'])

@stocks_router.get("/{symbol}", response_model=CreateStock)
async def read_stock(symbol: str, request: Request, db: Session = Depends(get_db)) -> CreateStock:
    start_time = time.time()
    db_stock = crud.get_stock_by_symbol(db, symbol=symbol)
    
    if db_stock is None or db_stock.from_ != (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'):
        stock_data = fetch_stock_from_polygon(symbol)
        db_stock = crud.create_stock(db, stock_data)

    response_status = 200
    await log_event(db, request, response_status, time.time() - start_time)
    return db_stock


@stocks_router.post("/{symbol}", response_model=dict)
async def update_stock(symbol: str, amount: AmountUpdateBase, request: Request, db: Session = Depends(get_db)) -> dict:
    start_time = time.time()
    crud.update_stock_amount(db, symbol=symbol, amount=amount.amount)

    order = OrderBase(stock_symbol=symbol, amount=amount.amount)
    crud.create_order(db, order)
    response_status = 201
    await log_event(db, request, response_status, time.time() - start_time)
    return {"message": f"{amount.amount} units of stock {symbol} were added to your stock record"}

async def log_event(db: Session, request: Request, response_status: int, response_time: float):
    event = EventBase(
        endpoint=str(request.url),
        method=request.method,
        status_code=response_status,
        response_time=response_time
    )
    crud.create_event(db, event)

def fetch_stock_from_polygon(symbol: str) -> StockBase:
    yesterday_date = (datetime.now(timezone.utc) - timedelta(days=1)).strftime('%Y-%m-%d')

    url = f"{constants.POLYGON_BASE_URL}/{symbol}/{yesterday_date}?apiKey={constants.POLYGON_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch stock data")

    data = response.json()
    if data["status"] != "OK":
        raise HTTPException(status_code=404, detail="Stock data not available")

    return StockBase(
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