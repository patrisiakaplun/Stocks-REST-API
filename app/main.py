import uvicorn
from fastapi import FastAPI
from app.routers.get_stock import get_stock_router
from app.routers.update_stock import update_stock_router
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(get_stock_router)
app.include_router(update_stock_router)

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8080)