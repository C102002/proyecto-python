from fastapi import FastAPI
from src.common.infrastructure import CorsConfig
from src.common.infrastructure import PostgresDatabase
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    database = PostgresDatabase()
    await database.create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

CorsConfig.setup_cors(app)

@app.get("/")
def root():
    return {"Hello": "World"}