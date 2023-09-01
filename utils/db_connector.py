import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_username = "postgres"
db_password = "postgres"
db_host = "localhost"  # usually "localhost" if it's running locally
db_port = "5432"  # default PostgreSQL port is 5432
db_name = "token_db"

# Create the database connection string
db_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
db_url_without_db = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}"

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def get_db_url():
    return db_url

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

