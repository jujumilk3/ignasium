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
    id: int = Field(default=None, description="id", example=1)
    created_at: datetime = Field(
        default=None, description="created_at", example="2020-01-01 00:00:00"
    )
    updated_at: datetime = Field(
        default=None, description="updated_at", example="2020-01-01 00:00:00"
    )


class BaseListResponse(BaseModel):
    offset: int = Field(default=0, description="offset", example=0)
    limit: int = Field(default=10, description="limit", example=10)
    total: int = Field(default=0, description="total", example=100)
    results: list = Field(default=[], description="results")


class AllOptional(ModelMetaclass):
    def __new__(mcs, name, bases, namespaces, **kwargs):
        annotations = namespaces.get("__annotations__", {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = Optional[annotations[field]]
        namespaces["__annotations__"] = annotations
        return super().__new__(mcs, name, bases, namespaces, **kwargs)


class MakeOptional(BaseModel):
    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs: Any) -> None:
        super().__pydantic_init_subclass__(**kwargs)

        for field in cls.model_fields.values():
            if field.is_required():
                field.default = None

        cls.model_rebuild(force=True)


from typing import Optional, Type
from pydantic import BaseModel, create_model, validator, Field
import inspect


def optional(*fields):
    def dec(cls):
        class OptionalModel(cls):
            class Config:
                extra = "allow"

        for field in fields:
            OptionalModel.__annotations__[field] = Optional[
                cls.__annotations__.get(field, str)
            ]
            OptionalModel.__config__.extra_fields[field].default = None

        return OptionalModel

    if fields and inspect.isclass(fields[0]) and issubclass(fields[0], BaseModel):
        cls = fields[0]
        fields = cls.__annotations__
        return dec(cls)

    return dec
