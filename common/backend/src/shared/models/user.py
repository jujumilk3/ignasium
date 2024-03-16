from shared.models.base import (
    BasePydanticModel,
    BaseSqlalchemyModel,
)
from datetime import datetime
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class User(BaseSqlalchemyModel):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String, nullable=False, index=True)
    user_token: Mapped[str] = mapped_column(String, nullable=True, index=True)
    email: Mapped[str] = mapped_column(String, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    oauth_platform: Mapped[str] = mapped_column(String, nullable=True)
    oauth_id: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)


class UserDto:
    class Base(BaseModel):
        username: str = Field(default=None, description="username", example="username")
        user_token: str = Field(
            default=None, description="user_token", example="user_token"
        )
        email: str = Field(default=None, description="email", example="email")
        password: str = Field(default=None, description="password", example="password")
        oauth_platform: str = Field(
            default=None, description="oauth_platform", example="oauth_platform"
        )
        oauth_id: str = Field(default=None, description="oauth_id", example="oauth_id")
        is_active: bool = Field(default=False, description="is_active", example=False)
        is_superuser: bool = Field(
            default=False, description="is_superuser", example=False
        )

    class Upsert(Base): ...

    class WithModelBaseInfo(Base, BasePydanticModel): ...
