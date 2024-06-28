from app.database import Base
from sqlalchemy import Column, Integer, String, Float, JSON


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    afterHours = Column(Float)
    close = Column(Float)
    from_ = Column(String)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    preMarket = Column(Float)
    status = Column(String)
    symbol = Column(String, unique=True, index=True)
    volume = Column(Integer)
    performance = Column(JSON, default={})
    amount = Column(Integer)