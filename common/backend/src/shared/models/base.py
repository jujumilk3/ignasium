from datetime import datetime

from shared.utils.string_utils import resolve_table_name
from pydantic import BaseModel, Field
from sqlalchemy import DateTime, String, TypeDecorator, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class BaseSqlalchemyModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False), default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


class BasePydanticModel(BaseModel):
    id: int = Field(default=None, description="id", example=1)
    created_at: datetime = Field(
        default=None, description="created_at", example="2020-01-01 00:00:00"
    )
    updated_at: datetime = Field(
        default=None, description="updated_at", example="2020-01-01 00:00:00"
    )
