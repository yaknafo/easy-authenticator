from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.role import Role

Base = declarative_base()


class User(Base):
    """role model representing a role table."""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True, nullable=False)
    password = Column(String(200))
    # Define the foreign key column
    role = Column(Integer, ForeignKey("role.id"))

    # Define a relationship to the Role table (optional, but useful)
    user_role = relationship(Role)
