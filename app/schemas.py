from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class StockBase(BaseModel):
    symbol: str
    afterHours: float
    close: float
    from_: str
    high: float
    low: float
    open: float
    preMarket: float
    status: str
    volume: int
    performance: Dict = {}
    amount: int

    class Config:
        from_attributes = True

class CreateStock(StockBase):
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    stock_symbol: str
    amount: int

    class Config:
        from_attributes = True

class CreateOrder(OrderBase):
    class Config:
        from_attributes = True

class EventBase(BaseModel):
    endpoint: str
    method: str
    status_code: int
    response_time: float

    class Config:
        from_attributes = True

class CreateEvent(EventBase):
    class Config:
        from_attributes = True
