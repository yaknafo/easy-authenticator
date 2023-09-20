from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Role(Base):
    """role model representing a role table."""

    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    token = Column(String(200))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False, unique=True)
    password = Column(Text)
    role_id = Column(Integer, ForeignKey('role.id'))  # Foreign key referencing the Role table

    # Define the relationship to the Role table
    # role = relationship("Role")