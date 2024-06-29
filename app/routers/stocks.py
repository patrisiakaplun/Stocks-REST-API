from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import crud, schemas, database
from datetime import datetime
import time

stocks_router = APIRouter(prefix='/stocks', tags=['stocks'])

@stocks_router.get("/{symbol}", response_model=schemas.Stock)
async def read_stock(symbol: str, request: Request, db: Session = Depends(get_db)):
    start_time = time.time()
    db_stock = crud.get_stock_by_symbol(db, symbol=symbol)
    if db_stock is None:
        response_status = 404
        await log_event(db, request, response_status, time.time() - start_time)
        raise HTTPException(status_code=response_status, detail="Stock not found")
    response_status = 200
    await log_event(db, request, response_status, time.time() - start_time)
    return db_stock

@stocks_router.post("/{symbol}", response_model=dict)
async def update_stock(symbol: str, amount: schemas.OrderCreate, request: Request, db: Session = Depends(get_db)):
    start_time = time.time()
    db_stock = crud.get_stock_by_symbol(db, symbol=symbol)
    if db_stock is None:
        response_status = 404
        await log_event(db, request, response_status, time.time() - start_time)
        raise HTTPException(status_code=response_status, detail="Stock not found")

    updated_stock = crud.update_stock_amount(db, symbol=symbol, amount=amount.amount)
    order = schemas.OrderCreate(stock_symbol=symbol, amount=amount.amount, timestamp=datetime.utcnow().isoformat())
    crud.create_order(db, order)
    response_status = 201
    await log_event(db, request, response_status, time.time() - start_time)
    return {"message": f"{amount.amount} units of stock {symbol} were added to your stock record"}