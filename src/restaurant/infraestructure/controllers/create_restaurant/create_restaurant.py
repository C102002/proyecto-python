# app/controllers/create_restaurant_controller.py
from fastapi import FastAPI
from fastapi import status

from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.database.postgres.postgres_database import PostgresDatabase
from src.common.infrastructure.id_generator.uuid_generator import UuidGenerator
from src.restaurant.application.services.create_restaurant_service import CreateRestaurantService
from src.restaurant.infraestructure.repositories.command.orm_restaurant_command_repository import OrmRestaurantCommandRepository
from ...routers.restaurant_router import restaurant_router
from ...dtos.request.create_restaurant_request_inf_dto import CreateRestaurantRequestInfDTO

class CreateRestaurantController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)
        
        session_generator = PostgresDatabase().get_session()
        # session = await anext(session_generator)
        # restaurant_command_repository = OrmRestaurantCommandRepository(session)
        id_generator = UuidGenerator()

        # self.user_login_service = CreateRestaurantService(
        #     restaurant_command_repository=restaurant_command_repository,
        #     id_generator=id_generator
        # )

    def setup_routes(self):
        @restaurant_router.post(
            "/",
            response_model=CreateRestaurantRequestInfDTO,
            status_code=status.HTTP_201_CREATED,
            summary="Crear restaurante",
            description=(
                "Crea un nuevo restaurante con:\n"
                "- latitud\n"
                "- longitud\n"
                "- nombre\n"
                "- hora de apertura\n"
                "- hora de cierre"
            ),
            response_description="Datos del restaurante recién creado"
        )
        async def create_restaurant(input_dto: CreateRestaurantRequestInfDTO):
            service=ExceptionDecorator()
            return input_dto
