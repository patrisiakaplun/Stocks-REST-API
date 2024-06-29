# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def get_stock_by_symbol(db: Session, symbol: str):
    return db.query(models.Stock).filter(models.Stock.symbol == symbol).first()

def create_stock(db: Session, stock: schemas.StockCreate):
    db_stock = models.Stock(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

def update_stock_amount(db: Session, symbol: str, amount: int):
    db_stock = db.query(models.Stock).filter(models.Stock.symbol == symbol).first()
    if db_stock:
        db_stock.amount += amount
        db.commit()
        db.refresh(db_stock)
    return db_stock

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
