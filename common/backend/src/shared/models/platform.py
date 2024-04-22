from shared.models.base import (
    AllOptional,
    BasePydanticModel,
    BaseSqlalchemyModel,
    BaseListResponse,
    MakeOptional,
    optional,
)
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional


class Platform(BaseSqlalchemyModel):
    __tablename__ = "platform"

    name: Mapped[str] = mapped_column(String, nullable=False, index=True, unique=True)
    is_child: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, index=True
    )
    parent_platform_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)


class PlatformDto:
    class Base(BaseModel):
        name: Optional[str] = Field(default=None, description="name", example="github")
        is_child: Optional[bool] = Field(
            default=False, description="is_child platform", example=False
        )
        parent_platform_id: Optional[int] = Field(
            default=None, description="parent_platform_id", example=1
        )

    class Upsert(Base): ...

    class WithModelBaseInfo(Base, BasePydanticModel): ...

    class ListResponse(Base, BaseListResponse):
        results: list["PlatformDto.WithModelBaseInfo"] = Field(
            default=[], description="results"
        )
