from sqlalchemy import Column, Integer, String

from .base import Base

class Activity(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True)

    activity = Column(String)
    time = Column(Integer)

    def __init__(self, activity, time):
        self.activity = activity
        self.time = time