import os
import pytest

# test line for ga test
os.environ["ENV"] = "test"
if os.getenv("ENV") not in ["test"]:
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)

import pytest_asyncio
import asyncio
from loguru import logger
from app.main import app
from tests.utils_for_test.router_for_test import router as basic_router_for_test
from fastapi.testclient import TestClient
from shared.repositories.platform_repository import PlatformRepository
from shared.models.platform import PlatformDto
from shared.models.base import BaseSqlalchemyModel


@pytest.fixture(scope="session")
def client():
    logger.info(f"ENV: {os.getenv('ENV')}")
    app.include_router(basic_router_for_test, prefix="/test_only")
    logger.info("client fixture created")
    asyncio.run(init_test_db())
    asyncio.run(insert_default_data())
    yield TestClient(app)


async def init_test_db():
    async with app.db.async_engine.begin() as conn:
        await conn.run_sync(BaseSqlalchemyModel.metadata.create_all)


async def insert_default_data():
    platform_repository: PlatformRepository = app.container.platform_repository()

    platforms = [
        PlatformDto.Upsert(
            name="github",
        ),
        PlatformDto.Upsert(
            name="aws",
        ),
        PlatformDto.Upsert(
            name="bloomberg",
        ),
    ]
    for platform in platforms:
        await platform_repository.insert(dto=platform)


@pytest.fixture
def simple_fixture():
    logger.info("simple_fixture called")
    logger.info(f"simple_fixture id: {(id(simple_fixture))}")
    yield "simple_fixture"


@pytest_asyncio.fixture
async def a_simple_fixture():
    logger.info("a_simple_fixture called")
    logger.info(f"a_simple_fixture id: {(id(a_simple_fixture))}")
    yield "a_simple_fixture"
