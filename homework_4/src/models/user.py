from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid as uuid
from pydantic import UUID4
from sqlmodel import Field, SQLModel

__all__ = ("User",)


def new_uuid() -> uuid.UUID:
    val = uuid.uuid4()
    while val.hex[0] == "0":
        val = uuid.uuid4()
    return str(val)


# class User(declarative_base()):
#     uuid = Column(default_factory=new_uuid, primary_key=True)
#     username = Column(String)
#     password = Column(String)
#     created_at = Column(DateTime, default=datetime.utcnow()),
#     is_superuser = Column(Boolean, default=False),
#     is_totp_enabled = Column(Boolean, default=False),
#     is_active = Column(Boolean, default=True),
#     email = Column(String)


class User(SQLModel, table=True):
    uuid: str = Field(default_factory=new_uuid, primary_key=True)
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    is_superuser: bool = False
    is_totp_enabled: bool = True
    is_active: bool = True
    email: str = Field(nullable=True)
