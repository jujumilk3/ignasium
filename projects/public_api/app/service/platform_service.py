from shared.repositories import PlatformRepository

from app.service.base_service import BaseService


class PlatformService(BaseService):
    def __init__(self, repository: PlatformRepository):
        self.repository = repository

    async def get_platform_list(
        self,
        offset: int = 0,
        limit: int = 20,
        name: str = None,
    ):
        pass
