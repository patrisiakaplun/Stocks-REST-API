from app.database import Base
from sqlalchemy import Column, Integer, String, Float

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    stock_symbol = Column(String)
    amount = Column(Integer)
    timestamp = Column(String)