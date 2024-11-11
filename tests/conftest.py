import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app.main import app
from app.infrastructure.database.mongo_connection import MongoConnection

TEST_MONGO_URI = "mongodb://localhost:27017/test_intelistyle_db"

test_mongo_connection = MongoConnection(uri=TEST_MONGO_URI)


@pytest.fixture(scope="session", autouse=True)
async def setup_test_database():
    db = await test_mongo_connection.get_database()
    garments_collection = db["garments"]
    yield


@pytest.fixture(scope="function")
async def db():
    """Provide a clean database instance for each test."""
    db = await test_mongo_connection.get_database()
    yield db


@pytest.fixture(scope="function")
def client(db):
    """Provide a TestClient with the test MongoDB dependency."""
    async def override_get_mongo_db():
        yield db

    app.dependency_overrides[test_mongo_connection.get_database] = override_get_mongo_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        print("Client is ready")
        yield client