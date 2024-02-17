import pytest_asyncio
from loguru import logger


@pytest_asyncio.fixture
async def a_simple_fixture():
    logger.info("a_simple_fixture called")
    logger.info(f"a_simple_fixture id: {(id(a_simple_fixture))}")
    yield "a_simple_fixture"
