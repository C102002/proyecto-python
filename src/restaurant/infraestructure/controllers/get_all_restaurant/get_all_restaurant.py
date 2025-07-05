from typing import List

from fastapi import Depends, FastAPI, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.restaurant.application.services.get_all_restaurant_service import GetAllRestaurantService
from src.restaurant.infraestructure.dtos.request.get_all_restaurant_request_inf_dto import GetAllRestaurantRequestInfDTO
from src.restaurant.infraestructure.dtos.response.get_all_restaurant_response_inf_dto import GetAllRestaurantResponseInfDTO
from src.restaurant.infraestructure.repositories.query.orm_restaurant_query_repository import OrmRestaurantQueryRepository
from ...routers.restaurant_router import restaurant_router


class GetAllRestaurantController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)

    async def get_query_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession()),
    ) -> GetAllRestaurantService:
        repo = OrmRestaurantQueryRepository(session)
        return GetAllRestaurantService(restaurant_query_repository=repo)

    def setup_routes(self):
        @restaurant_router.get(
            "/",
            response_model=List[GetAllRestaurantResponseInfDTO],
            status_code=status.HTTP_200_OK,
            summary="Listar restaurantes",
            description="Devuelve todos los restaurantes sin incluir sus mesas",
            response_description="Listado de restaurantes"
        )
        async def get_all_restaurants(
            # <— inyectamos el DTO como dependencia, FastAPI lo llena desde ?page=…&size=…
            input_dto: GetAllRestaurantRequestInfDTO = Depends(),
            service: GetAllRestaurantService = Depends(self.get_query_service),
        ):
            decorated = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )
            result = await decorated.execute(input_dto)
            restaurants = result.value

            return [
                GetAllRestaurantResponseInfDTO(
                    id=rest.id,
                    lat=rest.lat,
                    lng=rest.lng,
                    name=rest.name,
                    opening_time=rest.opening_time,
                    closing_time=rest.closing_time
                )
                for rest in restaurants
            ]
