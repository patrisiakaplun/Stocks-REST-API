from database import Base
from typing import Optional

class Stock(Base):
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
    performance: dict = {}
    amount: Optional[int] = None