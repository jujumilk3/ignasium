from dependency_injector import containers, providers
from shared.core.container import Container as SharedContainer


class Container(SharedContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoint.platform",
            "app.api.v1.endpoint.user",
        ]
    )
