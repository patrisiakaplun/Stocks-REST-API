from app.database import Base
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, text

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    endpoint = Column(String)
    method = Column(String)
    status_code = Column(Integer)
    response_time = Column(Float)

    def __repr__(self):
        return (f"Event(id={self.id}, timestamp={self.timestamp}, endpoint='{self.endpoint}', "
                f"method='{self.method}', status_code={self.status_code}, response_time={self.response_time})")