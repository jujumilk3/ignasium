from shared.repositories import PlatformRepository

from app.service.base_service import BaseService


class PlatformService(BaseService):
    def __init__(self, repository: PlatformRepository):
        self.repository: PlatformRepository = repository
