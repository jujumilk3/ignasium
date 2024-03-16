from contextlib import AbstractContextManager
from typing import Callable

from loguru import logger
from pydantic import BaseModel
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from shared.core.exceptions import DatabaseNotFoundError


class BaseRepository:
    def __init__(
        self,
        sync_session_factory: Callable[..., AbstractContextManager[AsyncSession]],
        async_session_factory: Callable[..., AbstractContextManager[AsyncSession]],
        model,
    ) -> None:
        self.sync_session_factory = sync_session_factory
        self.async_session_factory = async_session_factory
        self._model = model
        self._model_name = model.__name__

    async def select_by_id(self, model_id: int):
        async with self.async_session_factory() as session:
            query = select(self._model).where(self._model.id == model_id)
            query_result = await session.execute(query)
            found_model = query_result.scalar()
            return found_model

    async def select_by_ids(self, model_ids: list[int]):
        async with self.async_session_factory() as session:
            query = select(self._model).where(self._model.id.in_(model_ids))
            query_result = await session.execute(query)
            found_model_list = query_result.scalars().all()
            return found_model_list

    async def insert(self, dto):
        async with self.async_session_factory() as session:
            query = self._model(**dto.dict())
            session.add(query)
            await session.commit()
            await session.refresh(query)
            return query

    async def update(self, model_id: int, dto: BaseModel):
        async with self.async_session_factory() as session:
            found_model = await self.select_by_id(model_id)
            if found_model.id is None:
                raise ValueError(f"model id is None: {found_model}")
            for key, value in dto.model_dump().items():
                if value is None:
                    continue
                setattr(found_model, key, value)
            session.add(found_model)
            await session.commit()
            await session.refresh(found_model)
            return found_model

    async def update_by_using_model(self, model, dto: BaseModel):
        if model.id is None:
            raise ValueError(f"model id is None: {model}")
        async with self.async_session_factory() as session:
            for key, value in dto.model_dump().items():
                if value is None:
                    continue
                setattr(model, key, value)
            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model

    async def upsert(self, model_id: int, dto: BaseModel):
        async with self.async_session_factory() as session:
            found_model = await self.select_by_id(model_id)
            if found_model is None:
                return await self.insert(dto=dto)
            return self.update(model_id=model_id, dto=dto)

    async def delete_by_id(self, model_id: int):
        async with self.async_session_factory() as session:
            found_model = await self.select_by_id(model_id)
            if found_model is None:
                raise DatabaseNotFoundError(
                    f"model not found. model name: {self._model_name}. requested id: {model_id}"
                )
            await session.delete(found_model)
            await session.commit()
