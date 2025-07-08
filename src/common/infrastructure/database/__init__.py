from .postgres.postgres_database import PostgresDatabase
from typing import AsyncGenerator
from sqlmodel.ext.asyncio.session import AsyncSession

db_instance = PostgresDatabase()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with db_instance.get_session() as session:
        yield session
