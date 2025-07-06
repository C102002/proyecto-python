# app/controllers/create_restaurant_controller.py
from fastapi import Depends, FastAPI
from fastapi import status

from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.database.postgres.postgres_database import PostgresDatabase
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.id_generator.secuential_integer_generator import SequentialIntegerGenerator
from src.common.infrastructure.id_generator.uuid_generator import UuidGenerator
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession
from src.restaurant.application.dtos.request.create_restaurant_request_dto import CreateRestaurantRequestDTO
from src.restaurant.application.dtos.request.create_table_dto import CreateTableDTO
from src.restaurant.application.dtos.request.create_table_request_dto import CreateTableRequestDTO
from src.restaurant.application.services.create_restaurant_service import CreateRestaurantService
from src.restaurant.infraestructure.dtos.response.create_restaurant_response_inf_dto import CreateRestaurantResponseInfDTO
from src.restaurant.infraestructure.dtos.response.create_table_response_inf_dto import CreateTableResponseInfDTO
from src.restaurant.infraestructure.repositories.command.orm_restaurant_command_repository import OrmRestaurantCommandRepository
from ...routers.restaurant_router import restaurant_router
from ...dtos.request.create_restaurant_request_inf_dto import CreateRestaurantRequestInfDTO
from sqlalchemy.ext.asyncio import AsyncSession

class CreateRestaurantController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)
        
    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession()))->CreateRestaurantService:
        id_generator = UuidGenerator()
        orm_restaurant_command_repository = OrmRestaurantCommandRepository(postgres_session)
        tables_id_generator=SequentialIntegerGenerator()
        user_create_restaurant_service = CreateRestaurantService(
            id_generator=id_generator,
            restaurant_command_repository=orm_restaurant_command_repository,
            tables_id_generator=tables_id_generator
        )

        return user_create_restaurant_service

    def setup_routes(self):
        @restaurant_router.post(
            "/",
            response_model=CreateRestaurantResponseInfDTO,
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
        async def create_restaurant(input_dto: CreateRestaurantRequestInfDTO,create_restaurant_service: CreateRestaurantService = Depends(self.get_service)):
        
            service=ExceptionDecorator(service=create_restaurant_service,error_handler=FastApiErrorHandler())
            
            request = CreateRestaurantRequestDTO(
                lat=input_dto.lat,
                lng=input_dto.lng,
                name=input_dto.name,
                opening_time=input_dto.opening_time,
                closing_time=input_dto.closing_time,
                tables=(
                    [CreateTableDTO(
                        number=tbl.number,
                        capacity=tbl.capacity,
                        location=tbl.location
                    ) for tbl in input_dto.tables]
                    if input_dto.tables else []
                )
            )
                        
            result = await service.execute(request)
            
            result_response = result.value

            response = CreateRestaurantResponseInfDTO(
                id=result_response.id,
                lat=result_response.lat,
                lng=result_response.lng,
                name=result_response.name,
                opening_time=result_response.opening_time,
                closing_time=result_response.closing_time,
                tables=[
                    CreateTableResponseInfDTO(
                        id=tbl.id,
                        capacity=tbl.capacity,
                        location=tbl.location,
                        restaurant_id=tbl.restaurant_id
                    )
                    for tbl in result_response.tables
                ]
            )

            return response
