from app.database import Base
from sqlalchemy import Column, Integer, String, Float, JSON


class Stock(Base):
    __tablename__ = "stocks"

    symbol = Column(String, primary_key=True, unique=True)
    afterHours = Column(Float)
    close = Column(Float)
    from_ = Column(String)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    preMarket = Column(Float)
    status = Column(String)
    volume = Column(Integer)
    performance = Column(JSON, default={})
    amount = Column(Integer)

    def __repr__(self):
        return (f"Stock( symbol='{self.symbol}', afterHours={self.afterHours}, close={self.close}, "
                f"from_='{self.from_}', high={self.high}, low={self.low}, open={self.open}, preMarket={self.preMarket}, "
                f"status='{self.status}', volume={self.volume}, performance='{self.performance}', amount={self.amount})")