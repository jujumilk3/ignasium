from datetime import datetime

from shared.utils.string_utils import resolve_table_name
from pydantic import BaseModel, Field
from pydantic._internal._model_construction import ModelMetaclass
from sqlalchemy import DateTime, String, TypeDecorator, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column
from shared.constants.constants import UTC
from typing import Optional, Any


class BaseSqlalchemyModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(tz=UTC), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(tz=UTC),
        onupdate=datetime.now(tz=UTC),
        nullable=False,
    )


class BasePydanticModel(BaseModel):
    id: int = Field(default=None, description="id", examples=[1])
    created_at: datetime = Field(
        default=None, description="created_at", examples=["2020-01-01 00:00:00"]
    )
    updated_at: datetime = Field(
        default=None, description="updated_at", examples=["2020-01-01 00:00:00"]
    )


class BaseListResponse(BaseModel):
    offset: int = Field(default=0, description="offset", examples=[0])
    limit: int = Field(default=10, description="limit", examples=[10])
    total: int = Field(default=0, description="total", examples=[100])
    results: list = Field(default=[], description="results")
