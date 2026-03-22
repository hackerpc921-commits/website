from sqlalchemy import Column, Integer, String, DateTime, Text
from .database import Base
from datetime import datetime

class LabHistory(Base):
    __tablename__ = "lab_history"

    id = Column(Integer, primary_key=True, index=True)
    tool = Column(String)
    target = Column(String)
    output = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
