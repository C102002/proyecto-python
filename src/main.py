from fastapi import FastAPI
from src.common.infrastructure import CorsConfig
from src.common.infrastructure import PostgresDatabase
from contextlib import asynccontextmanager
from src.auth.infrastructure.controllers.register.user_register import UserRegisterController
from src.auth.infrastructure.controllers.login.user_login import UserLoginController
from src.auth.infrastructure.controllers.update.user_update import UserUpdateController
from src.restaurant.infraestructure.controllers.create_restaurant.create_restaurant import CreateRestaurantController
from src.restaurant.infraestructure.controllers.create_table.create_table import CreateTableController
from src.restaurant.infraestructure.controllers.delete_restaurant_by_id.delete_restaurant_by_id import DeleteRestaurantByIdController
from src.restaurant.infraestructure.controllers.delete_table_by_id.delete_table_by_id import DeleteTableByIdController
from src.restaurant.infraestructure.controllers.get_all_restaurant.get_all_restaurant import GetAllRestaurantController
import faulthandler

from src.restaurant.infraestructure.controllers.get_restaurant_by_id.get_restaurant_by_id import GetRestaurantByIdController
from src.menu.infrastructure.controllers.menu_controller import MenuController
from src.restaurant.infraestructure.controllers.update_restaurant.update_restaurant import UpdateRestaurantController
from src.restaurant.infraestructure.controllers.update_table.update_restaurant import UpdateTableController
faulthandler.enable()           # colócalo en tu módulo principal, p.ej. src/main.py


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Esta llamada asegura que el _engine y _async_session_factory se inicialicen
    PostgresDatabase()
    # Para llamar a create_db_and_tables, necesitamos una instancia.
    # Puede ser la misma que la de arriba, o una nueva (que usará el motor ya inicializado).
    initial_db_instance = PostgresDatabase()
    await initial_db_instance.create_db_and_tables()
    print("Base de datos y tablas creadas.")
    yield
    if PostgresDatabase._engine:
        await PostgresDatabase._engine.dispose()
        print("Motor de base de datos dispuesto en el shutdown de la app.")

app = FastAPI(lifespan=lifespan)

CorsConfig.setup_cors(app)

@app.get("/")
def root():
    return {"Hello": "World"}

# Auth Controllers
UserRegisterController(app)
UserUpdateController(app)
UserLoginController(app)

# Restaurants Controllers
CreateRestaurantController(app)
GetAllRestaurantController(app)
GetRestaurantByIdController(app)
DeleteRestaurantByIdController(app)

# Menu Controllers
MenuController(app)


# Table Controllers
DeleteTableByIdController(app)
CreateTableController(app)
UpdateRestaurantController(app)
UpdateTableController(app)