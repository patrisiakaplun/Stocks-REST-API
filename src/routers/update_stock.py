from fastapi import APIRouter

update_stock_router = APIRouter()

@update_stock_router.post("/stock/{stock_symbol}")
def update_stock(stock_symbol: str):
    return