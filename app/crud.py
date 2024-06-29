from sqlalchemy.orm import Session
from app import schemas
from app.models.stock import Stock
from app.models.order import Order
from app.models.event import Event

def get_stock_by_symbol(db: Session, symbol: str):
    return db.query(Stock).filter(Stock.symbol == symbol).first()

def create_stock(db: Session, stock: schemas.StockBase):
    db_stock = Stock(**stock.model_dump())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

def update_stock_amount(db: Session, symbol: str, amount: int):
    db_stock = db.query(Stock).filter(Stock.symbol == symbol).first()
    if db_stock:
        db_stock.amount += amount
        db.commit()
        db.refresh(db_stock)
    return db_stock

def create_order(db: Session, order: schemas.OrderBase):
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def create_event(db: Session, event: schemas.EventBase):
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
