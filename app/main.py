import uvicorn
from fastapi import FastAPI
from app.routers.stocks import stocks_router
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(stocks_router)

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8080)