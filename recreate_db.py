from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base
from alembic.config import Config
from alembic import command

# Define the SQLAlchemy database URL
db_url = 'sqlite:///task.db'

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Drop all tables defined in the SQLAlchemy models
Base.metadata.drop_all(engine)

# Create all tables defined in the SQLAlchemy models
Base.metadata.create_all(engine)

# Run Alembic migrations to upgrade the database to the latest version
alembic_cfg = Config("alembic.ini")
command.upgrade(alembic_cfg, "head")
