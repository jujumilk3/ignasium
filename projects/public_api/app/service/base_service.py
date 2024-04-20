from pydantic import BaseModel
from shared.repositories.base_repository import BaseRepository


class BaseService:
    def __init__(self, repository: BaseRepository) -> None:
        self.repository: BaseRepository = repository

    async def get_by_id(self, model_id: int):
        return await self.repository.select_by_id(model_id=model_id)

    async def get_by_ids(self, model_ids: list[int]):
        return await self.repository.select_by_ids(model_ids=model_ids)

    async def add(self, dto: BaseModel):
        return await self.repository.insert(dto=dto)

    async def patch(self, model_id: int, dto: BaseModel):
        return await self.repository.update(model_id=model_id, dto=dto)

    async def upsert(self, model_id: int, dto: BaseModel):
        return await self.repository.upsert(model_id=model_id, dto=dto)

    async def remove_by_id(self, model_id: int):
        return await self.repository.delete_by_id(model_id=model_id)

    async def toggle(self, model_id: int, user_token: str):
        found_model = await self.get_by_id(model_id=model_id)
        if found_model is not None:
            return await self.remove_by_id(model_id=model_id)
        else:
            return await self.add(dto=found_model)

    async def close_async_scoped_session(self):
        return await self.repository.close_async_scoped_session()
