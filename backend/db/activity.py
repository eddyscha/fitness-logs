from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Column, Integer, String

from .base import Base

@dataclass
class Activity(Base):
    __tablename__ = 'activity'

    id: int
    activity: str
    time: datetime

    id = Column(Integer, primary_key=True)

    activity = Column(String)
    time = Column(Integer)

    def __init__(self, activity, time):
        self.activity = activity
        self.time = time