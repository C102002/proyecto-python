# app/controllers/create_table_controller.py
from fastapi import Depends, FastAPI, Path, Security, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.restaurant.application.dtos.request.create_table_request_dto import CreateTableRequestDTO
from src.restaurant.application.services.create_table_service import CreateTableService
from src.restaurant.infraestructure.dtos.request.create_table_request_inf_dto import CreateTableRequestInfDTO
from src.restaurant.infraestructure.dtos.response.create_table_response_inf_dto import CreateTableResponseInfDTO
from src.restaurant.infraestructure.repositories.command.orm_restaurant_command_repository import OrmRestaurantCommandRepository
from src.restaurant.infraestructure.repositories.query.orm_restaurant_query_repository import OrmRestaurantQueryRepository
from src.restaurant.infraestructure.repositories.command.orm_restaurant_command_repository import OrmRestaurantCommandRepository

from ...routers.restaurant_router import restaurant_router


class CreateTableController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)

    async def get_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession()),
    ) -> CreateTableService:
        repo_query   = OrmRestaurantQueryRepository(session)
        repo_command = OrmRestaurantCommandRepository(session)
        return CreateTableService(
            restaurant_query_repository=repo_query,
            restaurant_command_repository=repo_command
        )

    def setup_routes(self):
        @restaurant_router.post(
            "/{restaurant_id}/tables",
            response_model=CreateTableResponseInfDTO,
            status_code=status.HTTP_201_CREATED,
            summary="Add a new table to a restaurant",
            description="Creates a table under the given restaurant UUID",
            response_description="Data of the newly created table"
        )
        async def create_table(
            input_dto: CreateTableRequestInfDTO,
            restaurant_id: str = Path(..., description="UUID of the restaurant"),
            service: CreateTableService = Depends(self.get_service),
            token = Security(UserRoleVerify(), scopes=["admin:manage"])
        ):
            decorator = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )

            # Map infra DTO → domain DTO
            request = CreateTableRequestDTO(
                restaurant_id=restaurant_id,
                number=input_dto.number,
                capacity=input_dto.capacity,
                location=input_dto.location
            )

            # Execute use case
            result = await decorator.execute(request)
            created = result.value
            
            # Map domain result → infra response DTO
            return CreateTableResponseInfDTO(
                number=created.id,
                capacity=created.capacity,
                location=created.location,
                restaurant_id=created.restaurant_id
            )
