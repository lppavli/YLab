from datetime import datetime
import uuid as uuid
from sqlmodel import Field, SQLModel

__all__ = ("User",)


def new_uuid() -> uuid.UUID:
    val = uuid.uuid4()
    while val.hex[0] == "0":
        val = uuid.uuid4()
    return str(val)


class User(SQLModel, table=True):
    uuid: str = Field(default_factory=new_uuid, primary_key=True)
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    is_superuser: bool = False
    is_totp_enabled: bool = True
    is_active: bool = True
    email: str = Field(nullable=True)
