from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from hello.database import Base


class AuthBase:
    __table_args__ = {"schema": "auth"}


class User(Base, AuthBase):
    __tablename__ = 'user'

    user_id = Column(UUID, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
