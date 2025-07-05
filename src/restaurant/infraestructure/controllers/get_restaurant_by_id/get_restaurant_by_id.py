# app/controllers/get_restaurant_by_id_controller.py
from fastapi import Depends, FastAPI, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.restaurant.application.dtos.request.get_restaurant_by_id_request_dto import GetRestaurantByIdRequestDTO
from src.restaurant.application.dtos.response.create_table_response_dto import CreateTableResponseDTO

from src.restaurant.application.services.get_restaurant_by_id_service import GetRestaurantByIdService

from src.restaurant.infraestructure.dtos.response.create_table_response_inf_dto import CreateTableResponseInfDTO
from src.restaurant.infraestructure.dtos.response.get_restaurant_by_id_response_inf_dto import GetRestaurantByIdResponseInfDTO
from src.restaurant.infraestructure.repositories.query.orm_restaurant_query_repository import OrmRestaurantQueryRepository
from ...routers.restaurant_router import restaurant_router


class GetRestaurantByIdController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)

    async def get_by_id_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession()),
    ) -> GetRestaurantByIdService:
        repo = OrmRestaurantQueryRepository(session)
        return GetRestaurantByIdService(restaurant_query_repository=repo)

    def setup_routes(self):
        @restaurant_router.get(
            "/{restaurant_id}",
            response_model=GetRestaurantByIdResponseInfDTO,
            status_code=status.HTTP_200_OK,
            summary="Obtener restaurante por ID",
            description="Devuelve un restaurante por su identificador incluyendo sus mesas",
            response_description="Datos del restaurante"
        )
        async def get_restaurant_by_id(
            restaurant_id: str = Path(..., description="ID del restaurante"),
            service: GetRestaurantByIdService = Depends(self.get_by_id_service),
        ):
            decorated = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )
            # Ejecuta la consulta por ID
            result = await decorated.execute(GetRestaurantByIdRequestDTO(restaurant_id))
            restaurant = result.value
            
            print(f"restaurant pepe:{restaurant}")
            
            return GetRestaurantByIdResponseInfDTO(
                id=restaurant.id,
                lat=restaurant.lat,
                lng=restaurant.lng,
                name=restaurant.name,
                opening_time=restaurant.opening_time,
                closing_time=restaurant.closing_time,
                tables=[
                    CreateTableResponseInfDTO(
                        number=int(table.id),
                        capacity=table.capacity,
                        location=table.location,
                        restaurant_id=restaurant.id
                    )
                    for table in restaurant.tables
                ]
            )
