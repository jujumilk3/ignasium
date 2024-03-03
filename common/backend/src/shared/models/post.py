from shared.models.base import (
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
