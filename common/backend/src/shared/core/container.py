from dependency_injector import containers, providers
from shared.core.database import Database
from shared.constants.configs import configs


class Container(containers.DeclarativeContainer):
    # db connections
    db = providers.Singleton(
        Database,
        db_address=configs.DATABASE_ADDRESS,
        sync_adapter=configs.DATABASE_SYNC_ADAPTER,
        async_adapter=configs.DATABASE_ASYNC_ADAPTER,
    )
