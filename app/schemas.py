from pydantic import BaseModel
from typing import Dict

class StockCreate(BaseModel):
    afterHours: float
    close: float
    from_: str
    high: float
    low: float
    open: float
    preMarket: float
    status: str
    symbol: str
    volume: int
    performance: Dict = {}
    amount: int

class Stock(StockCreate):
    id: int

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    stock_symbol: str
    amount: int
    timestamp: str

class Order(OrderCreate):
    id: int

    class Config:
        orm_mode = True

class EventCreate(BaseModel):
    timestamp: str
    endpoint: str
    method: str
    status_code: int
    response_time: float

class Event(EventCreate):
    id: int

    class Config:
        orm_mode = True