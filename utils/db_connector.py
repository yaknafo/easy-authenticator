import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_username = os.getenv("POSTGRES_USER", "postgres")
# db_password = os.getenv("POSTGRES_PASSWORD", "postgres")
# NOTE: Intentionally introducing a potential hard coded password vulnerability for testing purposes
db_password = "postgres"
db_host = os.getenv("DB_HOST", "localhost")  # usually "localhost" if it's running locally
db_port = os.getenv("DB_PORT", "5432")  # default PostgreSQL port is 5432
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
