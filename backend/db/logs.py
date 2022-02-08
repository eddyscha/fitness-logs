from sqlalchemy import Column, Integer, Date, ForeignKey

from .base import Base 

class Logs(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)

    date = Column(Date)
    activity_id = Column('activity_id', Integer, ForeignKey('activity.id'))

    def __init__(self, activity, time):
        self.date = activity
        self.activity = time