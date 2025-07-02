from fastapi import FastAPI
from src.common.infrastructure import CorsConfig
from src.common.infrastructure import PostgresDatabase
from contextlib import asynccontextmanager
from src.auth.infrastructure.controllers.register.user_register import UserRegisterController
from src.auth.infrastructure.controllers.login.user_login import UserLoginController

user_register_controller = None
user_login_controller = None
from src.restaurant.infraestructure.controllers.create_restaurant.create_restaurant import CreateRestaurantController
from src.restaurant.infraestructure.controllers.get_all_restaurants.get_all_restaurant import GetAllRestaurantController

@asynccontextmanager
async def lifespan(app: FastAPI):
    database = PostgresDatabase()
    await database.create_db_and_tables()

    global user_register_controller, user_login_controller
    user_register_controller = UserRegisterController(app)
    user_login_controller = UserLoginController(app)

    await user_register_controller.init()
    await user_login_controller.init()

    yield

app = FastAPI(lifespan=lifespan)

CorsConfig.setup_cors(app)

@app.get("/")
def root():
    return {"Hello": "World"}

UserRegisterController(app)
UserLoginController(app)


# Restaurants Controllers
CreateRestaurantController(app)
GetAllRestaurantController(app)