import uvicorn
from fastapi import FastAPI
from routers.update_stock import update_stock_router
from routers.get_stock import get_stock_router

app = FastAPI()

app.include_router(get_stock_router)
app.include_router(update_stock_router)

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8080)