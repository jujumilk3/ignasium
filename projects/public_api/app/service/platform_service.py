from shared.repositories import PlatformRepository

from app.service.base_service import BaseService


class PlatformService(BaseService):
    def __init__(self, repository: PlatformRepository):
        self.repository: PlatformRepository = repository

    async def get_by_name(self, name: str):
        return await self.repository.select_by_name(name=name)
