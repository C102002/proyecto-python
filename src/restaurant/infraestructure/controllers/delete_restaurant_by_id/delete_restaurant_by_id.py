# app/controllers/delete_restaurant_by_id_controller.py
from fastapi import Depends, FastAPI, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.restaurant.application.services.delete_restaurant_by_id_service import DeleteRestaurantByIdService
from src.restaurant.application.dtos.request.delete_restaurant_by_id_request_dto import DeleteRestaurantByIdRequestDTO
from src.restaurant.infraestructure.dtos.response.delete_restaurant_by_id_response_inf_dto import DeleteRestaurantByIdResponseInfDTO
from src.restaurant.infraestructure.repositories.command.orm_restaurant_command_repository import OrmRestaurantCommandRepository
from src.restaurant.infraestructure.repositories.query.orm_restaurant_query_repository import OrmRestaurantQueryRepository
from ...routers.restaurant_router import restaurant_router


class DeleteRestaurantByIdController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)

    async def get_delete_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession()),
    ) -> DeleteRestaurantByIdService:
        repo_query = OrmRestaurantQueryRepository(session)
        repo_command = OrmRestaurantCommandRepository(session)
        
        return DeleteRestaurantByIdService(restaurant_query_repository=repo_query,
                                           restaurant_command_repository=repo_command)

    def setup_routes(self):
        @restaurant_router.delete(
            "/{restaurant_id}",
            response_model=DeleteRestaurantByIdResponseInfDTO,
            status_code=status.HTTP_200_OK,
            summary="Delete a restaurant by ID",
            description="Deletes the restaurant with the given UUID",
            response_description="UUID of the deleted restaurant"
        )
        async def delete_restaurant_by_id(
            restaurant_id: str = Path(..., description="UUID of the restaurant to delete"),
            service: DeleteRestaurantByIdService = Depends(self.get_delete_service),
        ):
            decorator = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )
            result = await decorator.execute(DeleteRestaurantByIdRequestDTO(restaurant_id))
            deleted_id = result.value.restaurant_id

            return DeleteRestaurantByIdResponseInfDTO(
                restaurant_id=deleted_id
            )
