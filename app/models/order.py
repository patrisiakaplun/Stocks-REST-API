from app.database import Base
from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, text

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    stock_symbol = Column(String)
    amount = Column(Float)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=text('now()'))