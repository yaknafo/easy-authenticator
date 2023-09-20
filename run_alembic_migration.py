from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from utils.db_connector import get_db_url

db_name = "token_db"
# Try to create the database if it doesn't exist
try:
    engine = create_engine(get_db_url())
    if not database_exists(engine.url):
        create_database(engine.url)
    print(f"Database '{db_name}' created successfully.")
except OperationalError as e:
    print(f"Database '{db_name}' already exists or an error occurred: {e}")


# print('Running DB migrations in %r on %r', script_location, dsn)
alembic_cfg = Config()
alembic_cfg.set_main_option('script_location', "alembic")
alembic_cfg.set_main_option('sqlalchemy.url', get_db_url())
command.upgrade(alembic_cfg, 'head')

print("Alembic migrations have been applied.")
