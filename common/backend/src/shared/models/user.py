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
    profile_image: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)


class UserDto:
    class Base(BaseModel):
        username: str = Field(
            default=None, description="username", examples=["username"]
        )
        user_token: str = Field(
            default=None, description="user_token", examples=["user_token"]
        )
        email: str = Field(default=None, description="email", examples=["email"])
        password: str = Field(
            default=None, description="password", examples=["password"]
        )
        oauth_platform: str = Field(
            default=None, description="oauth_platform", examples=["oauth_platform"]
        )
        oauth_id: str = Field(
            default=None, description="oauth_id", examples=["oauth_id"]
        )
        profile_image: str = Field(
            default=None, description="profile_image", examples=["profile_image"]
        )
        is_active: bool = Field(
            default=False, description="is_active", examples=[False]
        )
        is_admin: bool = Field(default=False, description="is_admin", examples=[False])

    class Upsert(Base): ...

    class WithModelBaseInfo(Base, BasePydanticModel): ...
