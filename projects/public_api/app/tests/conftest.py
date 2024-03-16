import os
import pytest

# test line for ga test
os.environ["ENV"] = "test"
if os.getenv("ENV") not in ["test"]:
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)

import pytest_asyncio
from loguru import logger
from app.main import app
from tests.utils_for_test.router_for_test import router as basic_router_for_test
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def client():
    logger.info(f"ENV: {os.getenv('ENV')}")
    app.include_router(basic_router_for_test, prefix="/test_only")
    logger.info("client fixture created")
    yield TestClient(app)


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
