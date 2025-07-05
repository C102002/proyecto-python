# app/controllers/update_table_controller.py
from fastapi import Depends, FastAPI, Path, Body, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.restaurant.application.dtos.request.update_table_request_dto import UpdateTableRequestDTO
from src.restaurant.application.services.update_table_service import UpdateTableService

from src.restaurant.infraestructure.dtos.request.update_table_request_inf_dto import UpdateTableRequestInfDTO
from src.restaurant.infraestructure.dtos.response.update_table_response_inf_dto import UpdateTableResponseInfDTO

from src.restaurant.infraestructure.repositories.command.orm_restaurant_command_repository import OrmRestaurantCommandRepository
from src.restaurant.infraestructure.repositories.query.orm_restaurant_query_repository import OrmRestaurantQueryRepository


from ...routers.restaurant_router import restaurant_router


class UpdateTableController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)

    async def get_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession())
    ) -> UpdateTableService:
        repo_query   = OrmRestaurantQueryRepository(session)
        repo_command = OrmRestaurantCommandRepository(session)
        return UpdateTableService(
            restaurant_query_repository=repo_query,
            restaurant_command_repository=repo_command
        )

    def setup_routes(self):
        @restaurant_router.patch(
            "/{restaurant_id}/tables/{table_number}",
            response_model=UpdateTableResponseInfDTO,
            status_code=status.HTTP_200_OK,
            summary="Actualizar mesa",
            description="Actualiza número, capacidad o ubicación de una mesa existente",
            response_description="Datos de la mesa actualizada"
        )
        async def update_table(
            restaurant_id: str = Path(..., description="UUID del restaurante"),
            table_number: int = Path(..., description="Número de la mesa a actualizar"),
            input_dto: UpdateTableRequestInfDTO = Body(
                ..., description="Campos a actualizar (new_number, capacity, location)"
            ),
            service: UpdateTableService = Depends(self.get_service),
        ):
            decorator = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )

            # Mapear infra DTO → aplicación DTO
            request = UpdateTableRequestDTO(
                restaurant_id=restaurant_id,
                number=table_number,
                new_number=input_dto.new_number,
                capacity=input_dto.capacity,
                location=input_dto.location
            )

            # Ejecutar caso de uso
            result = await decorator.execute(request)
            updated = result.value
            
            print(f"updated: {updated}")

            # Mapear resultado de dominio → infra DTO
            return UpdateTableResponseInfDTO(
                restaurant_id=updated.restaurant_id,
                number=updated.id,
                capacity=updated.capacity,
                location=updated.location
            )
