from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Role(Base):
    """role model representing a role table."""

    __tablename__ = "role"
    id = Column(UUID, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    token = Column(String(200))
