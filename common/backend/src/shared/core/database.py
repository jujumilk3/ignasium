from asyncio import current_task


from sqlalchemy import create_engine, orm, MetaData
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    create_async_engine,
)
from sqlalchemy.pool import QueuePool


class Database:
    def __init__(
        self,
        db_address: str,
        sync_adapter: str,
        async_adapter: str,
    ) -> None:
        self.metadata = MetaData()

        # sync engine
        self.sync_engine = create_engine(
            url=f"{sync_adapter}://{db_address}",
            poolclass=QueuePool,
            pool_pre_ping=True,
        )
        # sync scoped session factory
        self.sync_session_factory = orm.scoped_session(
            session_factory=orm.sessionmaker(
                bind=self.sync_engine,
                class_=orm.Session,
                autocommit=False,
                autoflush=False,
            ),
            scopefunc=current_task,
        )

        # async engine
        self.async_engine = create_async_engine(
            url=f"{async_adapter}://{db_address}",
            poolclass=QueuePool,
            pool_pre_ping=True,
        )
        # async scoped session factory
        self.async_session_factory = async_scoped_session(
            session_factory=orm.sessionmaker(
                bind=self.async_engine,
                class_=AsyncSession,
                autocommit=False,
                autoflush=False,
            ),
            scopefunc=current_task,
        )
