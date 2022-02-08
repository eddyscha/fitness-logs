from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('postgresql://postgres:postgres@localhost:5432/fitness_logs')
if not database_exists(engine.url):
    create_database(engine.url)
    
Session = sessionmaker(bind=engine)

Base = declarative_base()