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
    platform_id: Mapped[int] = mapped_column(Integer, ForeignKey("platform.id"), nullable=False)
    published_at: Mapped[str] = mapped_column(DateTime(timezone=True), default=None, nullable=False)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, index=True)


class PostDto:
    class Base(BaseModel):
        title: str = Field(default=None, description="title", examples=["title"])
        content: str = Field(default=None, description="content", examples=["content"])
        platform_id: int = Field(default=None, description="platform_id", examples=[1])
        published_at: datetime = Field(default=None, description="published_at", examples=["2020-01-01 00:00:00"])
        is_published: bool = Field(default=False, description="is_published", examples=[False])

    class Upsert(Base): ...

    class WithModelBaseInfo(Base, BasePydanticModel): ...


class PostComponent:
    title: str | None = Field(default=None, description="title", examples=["title"])
    subtitle: str | None = Field(default=None, description="subtitle", examples=["subtitle"])
    thumbnail_url: str | None = Field(default=None, description="thumbnail_url", examples=["thumbnail_url"])
    authors_data: dict | None = Field(default=None, description="authors_data", examples=[{"name": "name"}])
    created_at: datetime | None = Field(default=None, description="created_at", examples=["2020-01-01 00:00:00+00:00"])
    updated_at: datetime | None = Field(default=None, description="updated_at", examples=["2020-01-01 00:00:00+00:00"])
    content: str | None = Field(default=None, description="content", examples=["content"])
    tags: list[str] | None = Field(default=None, description="tags", examples=[["tag1", "tag2"]])
