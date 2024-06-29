from app.database import Base
from sqlalchemy import Column, Integer, String, Float, JSON


class Stock(Base):
    __tablename__ = "stocks"

    symbol = Column(String, primary_key=True, unique=True)
    afterHours = Column(Float)
    close = Column(Float)
    from_ = Column(String)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    preMarket = Column(Float)
    status = Column(String)
    volume = Column(Integer)
    performance = Column(JSON, default={})
    amount = Column(Integer)