from fastapi import FastAPI
from src.common.infrastructure import CorsConfig
from src.common.infrastructure import PostgresDatabase
from contextlib import asynccontextmanager
from src.auth.infrastructure.controllers.register.user_register import UserRegisterController
from src.auth.infrastructure.controllers.login.user_login import UserLoginController
from src.restaurant.infraestructure.controllers.create_restaurant.create_restaurant import CreateRestaurantController
from src.restaurant.infraestructure.controllers.get_all_restaurants.get_all_restaurant import GetAllRestaurantController
import faulthandler
faulthandler.enable()           # colócalo en tu módulo principal, p.ej. src/main.py


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

# Auth Controllers
UserRegisterController(app)
UserLoginController(app)

# Restaurants Controllers
CreateRestaurantController(app)
GetAllRestaurantController(app)