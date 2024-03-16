from shared.repositories.base_repository import BaseRepository
from shared.models.user import User
from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import and_, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(BaseRepository):
    def __init__(
        self,
        sync_session_factory: Callable[..., AbstractContextManager[AsyncSession]],
        async_session_factory: Callable[..., AbstractContextManager[AsyncSession]],
    ) -> None:
        super().__init__(
            sync_session_factory=sync_session_factory,
            async_session_factory=async_session_factory,
            model=User,
        )
