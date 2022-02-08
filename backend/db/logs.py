from dataclasses import dataclass
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.activity import Activity

from .base import Base 

@dataclass
class Logs(Base):
    __tablename__ = 'logs'

    id: int
    activity: Activity

    id = Column(Integer, primary_key=True)

    date = Column(Date)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship("Activity", backref="logs")

    def __init__(self, date, activity):
        self.date = date
        self.activity = activity