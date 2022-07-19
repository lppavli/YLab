from datetime import datetime

from sqlmodel import Field, SQLModel

__all__ = ("Post",)


class Post(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    views: int = Field(default=0)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
