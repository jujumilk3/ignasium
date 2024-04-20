from dependency_injector import containers, providers
from shared.core.container import Container as SharedContainer

from app.service.platform_service import PlatformService


class Container(SharedContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoint.platform",
            "app.api.v1.endpoint.user",
        ]
    )

    platform_service = providers.Factory(
        PlatformService,
        repository=SharedContainer.platform_repository,
    )
