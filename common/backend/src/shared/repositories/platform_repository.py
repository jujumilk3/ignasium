from shared.repositories.base_repository import BaseRepository
from shared.models.platform import Platform
from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import and_, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class PlatformRepository(BaseRepository):
    def __init__(
        self,
        sync_session_factory: Callable[..., AbstractContextManager[AsyncSession]],
        async_session_factory: Callable[..., AbstractContextManager[AsyncSession]],
    ) -> None:
        super().__init__(
            sync_session_factory=sync_session_factory,
            async_session_factory=async_session_factory,
            model=Platform,
        )

    async def select_by_name(self, name: str):
        where_clauses = [
            Platform.name == name,
        ]
        async with self.async_session_factory() as session:
            query = select(Platform).where(*where_clauses)
            query_result = await session.execute(query)
            found_platform = query_result.scalar()
            return found_platform
