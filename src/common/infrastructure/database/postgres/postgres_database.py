from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession 
from sqlalchemy.ext.asyncio import create_async_engine
from typing import AsyncGenerator
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker 
from contextlib import asynccontextmanager

load_dotenv()

class PostgresDatabase:
    _url: str | None = None
    _engine = None
    _async_session_factory = None

    def __init__(self):
        if PostgresDatabase._url is None:
            PostgresDatabase._url = os.getenv("DATABASE_URL")
            if PostgresDatabase._url is None:
                raise ValueError("La variable de entorno DATABASE_URL no está definida")
        
        if PostgresDatabase._engine is None:
            PostgresDatabase._engine = create_async_engine(PostgresDatabase._url, echo=False, pool_pre_ping=True)
            
            PostgresDatabase._async_session_factory = sessionmaker(
                PostgresDatabase._engine, 
                class_=AsyncSession,
                expire_on_commit=False
            ) # type: ignore [call-arg]
            print("Motor de base de datos y fábrica de sesiones inicializados.")

    async def create_db_and_tables(self):
        if PostgresDatabase._engine is None:
            raise RuntimeError("El motor de la base de datos no está inicializado.")
        async with PostgresDatabase._engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
            print("Tablas de base de datos creadas/actualizadas.")

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        if PostgresDatabase._async_session_factory is None:
            raise RuntimeError("La fábrica de sesiones no está inicializada.")
        
        async with PostgresDatabase._async_session_factory() as session:
            try:
                yield session
            except Exception:
                await session.rollback() 
                raise
            finally:
                pass 