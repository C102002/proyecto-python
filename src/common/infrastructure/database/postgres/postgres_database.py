from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine 
from typing import AsyncGenerator
import os
from dotenv import load_dotenv

load_dotenv()

class PostgresDatabase:
    def __init__(self):
        self.url = os.getenv("DATABASE_URL")

        if self.url is None:
            raise ValueError("La variable de entorno DATABASE_URL no esta definida")
        
        self.engine = create_async_engine(self.url, echo=True)

    async def create_db_and_tables(self):

        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        
        async with AsyncSession(self.engine) as session:
            yield session