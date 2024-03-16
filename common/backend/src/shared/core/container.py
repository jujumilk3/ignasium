from dependency_injector import containers, providers
from shared.core.database import Database
from shared.constants.configs import configs
from shared import repositories as repository
from shared.repositories import UserRepository, PlatformRepository


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
        UserRepository,
        sync_session_factory=db.provided.sync_session_factory,
        async_session_factory=db.provided.async_session_factory,
    )
    platform_repository = providers.Factory(
        PlatformRepository,
        sync_session_factory=db.provided.sync_session_factory,
        async_session_factory=db.provided.async_session_factory,
    )
