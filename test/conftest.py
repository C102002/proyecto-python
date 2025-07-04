# conftest.py
import pytest
from sqlalchemy import text
import asyncio
import platform
from dotenv import load_dotenv
import pytest_asyncio # Import pytest_asyncio

# Import your FastAPI app and the PostgresDatabase class
from src.main import app
from src.common.infrastructure import PostgresDatabase
from sqlmodel import SQLModel

# Import TestClient for FastAPI integration tests
from fastapi.testclient import TestClient

# Load environment variables
load_dotenv()

# --- Platform-specific event loop policy for Windows ---
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# --- Initialize PostgresDatabase instance for the test session ---
db_instance = PostgresDatabase()
print(f"Using database URL: {db_instance._url}")

# --- FastAPI TestClient setup ---
client = TestClient(app)

# Use pytest_asyncio.fixture for async fixtures
@pytest_asyncio.fixture(scope="session", autouse=True) # Changed from @pytest.fixture
async def setup_and_teardown_db():
    """
    This fixture runs before each test function.
    It truncates all tables in the database to ensure a clean state
    for every test, using the SQLModel metadata.
    """
    await db_instance.create_db_and_tables()

    engine = PostgresDatabase._engine
    if engine is None:
        raise RuntimeError("Database engine is not initialized for tests.")

    async with engine.begin() as conn:
        for table in reversed(SQLModel.metadata.sorted_tables):
            try:
                if not table.name.startswith("alembic_"):
                    await conn.execute(text(f'TRUNCATE TABLE "{table.name}" RESTART IDENTITY CASCADE;'))
            except Exception as e:
                print(f"Error truncating table {table.name}: {e}")
                raise

    yield

# Use pytest_asyncio.fixture for async fixtures
@pytest_asyncio.fixture(scope="session") # Changed from @pytest.fixture
async def shutdown_db_engine():
    """
    This fixture runs once at the very end of the test session.
    It disposes the database engine to release resources.
    """
    yield
    if PostgresDatabase._engine:
        await PostgresDatabase._engine.dispose()
        PostgresDatabase._engine = None
        print("Database engine disposed at the end of the test session.")