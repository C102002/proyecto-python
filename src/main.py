from fastapi import FastAPI
from src.common.infrastructure import CorsConfig
from src.common.infrastructure import PostgresDatabase
from contextlib import asynccontextmanager
from src.auth.infrastructure.controllers.register.user_register_controller import UserRegisterController
from src.auth.infrastructure.controllers.login.user_login import UserLoginController

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

UserRegisterController(app)
UserLoginController(app)