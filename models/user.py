from sqlalchemy.orm import Mapped, mapped_column
from models.db import Base
from pydantic import BaseModel


# Table
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]


# Validation
class UserValidation(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
