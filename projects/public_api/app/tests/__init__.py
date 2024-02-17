import pytest_asyncio


@pytest_asyncio.fixture
async def asimple_fixture(client):
    logger.info("asimple_fixture called")
    logger.info(f"asimple_fixture id: {(id(asimple_fixture))}")
    yield "asimple_fixture"
