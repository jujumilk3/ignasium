from shared.models.base import (
    BasePydanticModel,
    BaseSqlalchemyModel,
)
from datetime import datetime
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Reaction(BaseSqlalchemyModel):
    __tablename__ = "reaction"

    content_type: Mapped[str] = mapped_column(String, nullable=False)
    content_id: Mapped[int] = mapped_column(Integer, nullable=False)
    user_token: Mapped[str] = mapped_column(String, nullable=False)
    reaction_type: Mapped[str] = mapped_column(String, nullable=False)


class ReactionDto:
    class Base(BaseModel):
        content_type: str = Field(
            default=None, description="content_type", example="content_type"
        )
        content_id: int = Field(default=None, description="content_id", example=1)
        user_token: str = Field(
            default=None, description="user_token", example="user_token"
        )
        reaction_type: str = Field(
            default=None, description="reaction_type", example="reaction_type"
        )

    class Upsert(Base): ...

    class WithModelBaseInfo(Base, BasePydanticModel): ...
