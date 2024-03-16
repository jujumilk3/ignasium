from shared.models.base import (
    BasePydanticModel,
    BaseSqlalchemyModel,
)
from datetime import datetime
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Post(BaseSqlalchemyModel):
    __tablename__ = "post"

    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    platform_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("platform.id"), nullable=False
    )
    published_at: Mapped[str] = mapped_column(
        DateTime(timezone=False), default=datetime.utcnow, nullable=False
    )
    is_published: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, index=True
    )


class PostDto:
    class Base(BaseModel):
        title: str = Field(default=None, description="title", example="title")
        content: str = Field(default=None, description="content", example="content")
        platform_id: int = Field(default=None, description="platform_id", example=1)
        published_at: datetime = Field(
            default=None, description="published_at", example="2020-01-01 00:00:00"
        )
        is_published: bool = Field(
            default=False, description="is_published", example=False
        )

    class Upsert(Base): ...

    class WithModelBaseInfo(Base, BasePydanticModel): ...
