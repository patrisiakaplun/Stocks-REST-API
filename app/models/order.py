from app.database import Base
from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, text

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    stock_symbol = Column(String)
    amount = Column(Float)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __repr__(self):
        return (f"Order(id={self.id}, stock_symbol='{self.stock_symbol}', amount={self.amount}, "
                f"timestamp={self.timestamp})")