# app/controllers/update_restaurant_controller.py
from fastapi import Depends, FastAPI, Path, Body, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.restaurant.application.dtos.request.update_restaurant_request_dto import UpdateRestaurantRequestDTO
from src.restaurant.application.services.update_restaurant_service import UpdateRestaurantService

from src.restaurant.infraestructure.dtos.request.update_restaurant_request_inf_dto import UpdateRestaurantRequestInfDTO
from src.restaurant.infraestructure.dtos.response.update_restaurant_response_inf_dto import UpdateRestaurantResponseInfDTO

from src.restaurant.infraestructure.repositories.query.orm_restaurant_query_repository import OrmRestaurantQueryRepository
from src.restaurant.infraestructure.repositories.command.orm_restaurant_command_repository import OrmRestaurantCommandRepository

from ...routers.restaurant_router import restaurant_router


class UpdateRestaurantController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)

    async def get_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession())
    ) -> UpdateRestaurantService:
        repo_query   = OrmRestaurantQueryRepository(session)
        repo_command = OrmRestaurantCommandRepository(session)
        return UpdateRestaurantService(
            restaurant_query_repository=repo_query,
            restaurant_command_repository=repo_command
        )

    def setup_routes(self):
        @restaurant_router.patch(
            "/{restaurant_id}",
            response_model=UpdateRestaurantResponseInfDTO,
            status_code=status.HTTP_200_OK,
            summary="Actualizar restaurante",
            description="Actualiza los datos de un restaurante existente",
            response_description="Datos del restaurante actualizado"
        )
        async def update_restaurant(
            restaurant_id: str = Path(..., description="UUID del restaurante a actualizar"),
            input_dto: UpdateRestaurantRequestInfDTO = Body(
                ..., description="Campos a actualizar (todos opcionales)"
            ),
            service: UpdateRestaurantService = Depends(self.get_service),
        ):
            decorator = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )

            # Mapear infra DTO → aplicación DTO
            request = UpdateRestaurantRequestDTO(
                id=restaurant_id,
                lat=input_dto.lat,
                lng=input_dto.lng,
                name=input_dto.name,
                opening_time=input_dto.opening_time,
                closing_time=input_dto.closing_time
            )

            # Ejecutar caso de uso
            result = await decorator.execute(request)
            updated = result.value

            # Mapear resultado de dominio → infra DTO
            return UpdateRestaurantResponseInfDTO(
                id=updated.id,
                lat=updated.lat,
                lng=updated.lng,
                name=updated.name,
                opening_time=updated.opening_time,
                closing_time=updated.closing_time
            )
