from dependency_injector import containers, providers
from shared.core.database import Database
from shared.constants.configs import configs
from shared import repositories as repository


class Container(containers.DeclarativeContainer):
    # db connections
    db = providers.Singleton(
        Database,
        db_address=configs.DATABASE_ADDRESS,
        sync_adapter=configs.DATABASE_SYNC_ADAPTER,
        async_adapter=configs.DATABASE_ASYNC_ADAPTER,
    )

    # repositories
    user_repository = providers.Factory(
        repository.UserRepository,
        sync_session_factory=db.sync_session_factory,
        async_session_factory=db.async_session_factory,
    )
    platform_repository = providers.Factory(
        repository.PlatformRepository,
        sync_session_factory=db.sync_session_factory,
        async_session_factory=db.async_session_factory,
    )
