from shared.repositories.base_repository import BaseRepository
from shared.models.platform import Platform
from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import and_, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class PlatformRepository(BaseRepository):
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[AsyncSession]],
        reader_session_factory: Callable[..., AbstractContextManager[AsyncSession]],
    ) -> None:
        super().__init__(session_factory, reader_session_factory, Platform)
