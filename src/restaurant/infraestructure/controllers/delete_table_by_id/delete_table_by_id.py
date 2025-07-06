# app/controllers/delete_table_by_id_controller.py
from fastapi import Depends, FastAPI, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.restaurant.application.services.delete_table_by_id_service import DeleteTableByIdService
from src.restaurant.application.dtos.request.delete_table_by_id_request_dto import DeleteTableByIdRequestDTO
from src.restaurant.infraestructure.dtos.response.delete_table_by_id_response_inf_dto import DeleteTableByIdResponseInfDTO

from src.restaurant.infraestructure.repositories.command.orm_restaurant_command_repository import OrmRestaurantCommandRepository
from src.restaurant.infraestructure.repositories.query.orm_restaurant_query_repository import OrmRestaurantQueryRepository

from ...routers.restaurant_router import restaurant_router


class DeleteTableByIdController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)

    async def get_delete_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession()),
    ) -> DeleteTableByIdService:
        repo_query   = OrmRestaurantQueryRepository(session)
        repo_command = OrmRestaurantCommandRepository(session)
        return DeleteTableByIdService(
            restaurant_query_repository=repo_query,
            restaurant_command_repository=repo_command
        )

    def setup_routes(self):
        @restaurant_router.delete(
            "/{restaurant_id}/tables/{table_id}",
            response_model=DeleteTableByIdResponseInfDTO,
            status_code=status.HTTP_200_OK,
            summary="Delete a table by ID",
            description="Deletes a specific table from a restaurant",
            response_description="UUID of the restaurant and ID of the deleted table"
        )
        async def delete_table_by_id(
            restaurant_id: str = Path(..., description="UUID of the restaurant"),
            table_id: int      = Path(..., description="Identifier of the table to delete"),
            service: DeleteTableByIdService = Depends(self.get_delete_service),
        ):
            decorator = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )
            # Execute the delete operation
            request_dto = DeleteTableByIdRequestDTO(restaurant_id, table_id)
            result = await decorator.execute(request_dto)
            deleted = result.value

            return DeleteTableByIdResponseInfDTO(
                restaurant_id=deleted.restaurant_id,
                table_id=deleted.table_id
            )
