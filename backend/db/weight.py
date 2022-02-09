from datetime import date as datetime_date

from dataclasses import dataclass
from sqlalchemy import Column, Integer, Date

from .base import Base 

@dataclass
class Logs(Base):
    __tablename__ = 'weight'

    id: int
    weight: int
    date: datetime_date

    id = Column(Integer, primary_key=True)

    weight = Column(Integer)
    date = Column(Date)


    def __init__(self, weight, date):
        self.weight = weight
        self.date = date
