from fastapi import APIRouter

get_stock_router = APIRouter()

@get_stock_router.get("/stock/{stock_symbol}")
async def get_stock(stock_symbol: str):
    return "hi"
