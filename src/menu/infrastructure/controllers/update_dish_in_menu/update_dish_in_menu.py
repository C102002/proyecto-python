from fastapi import FastAPI, Depends, status, Security
from src.menu.application.dtos.request.update_dish_request_dto import UpdateDishRequestDto
from ...dtos.request.update_dish_request_inf_dto import UpdateDishRequestInfDto
from src.menu.application.dtos.response.dish_response_dto import DishResponseDto
from src.menu.application.services.update_dish_in_menu_service import UpdateDishInMenuService
from src.common.application import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from ...routers.menu_router import menu_router
from sqlalchemy.ext.asyncio import AsyncSession
from ...repositories.command.orm_menu_command_repository import OrmMenuCommandRepository
from ...repositories.query.orm_menu_query_repository import OrmMenuQueryRepository
from src.common.infrastructure import GetPostgresqlSession
from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify

class UpdateDishInMenuController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(menu_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        orm_menu_query_repository = OrmMenuQueryRepository(postgres_session)
        orm_menu_command_repository = OrmMenuCommandRepository(postgres_session)

        update_dish_in_menu_service = UpdateDishInMenuService(
            orm_menu_command_repository,
            orm_menu_query_repository
        )

        return update_dish_in_menu_service

    def setup_routes(self):
        @menu_router.put(
            "/dishes/{dish_id}",
            response_model=DishResponseDto,
            status_code=status.HTTP_202_ACCEPTED,
            summary="Remove dish from menu",
        )
        async def update_dish_in_menu(dish_id: str, dish_dto: UpdateDishRequestInfDto, token = Security(UserRoleVerify(), scopes=["admin:manage"]), menu_service: UpdateDishInMenuService = Depends(self.get_service)):

            request = UpdateDishRequestDto(
                dish_id=dish_id,
                category=dish_dto.category,
                description=dish_dto.description,
                image=dish_dto.image,
                name=dish_dto.name,
                price=dish_dto.price
            )
            service = ExceptionDecorator(menu_service, FastApiErrorHandler())
            dish = await service.execute(request)
            return DishResponseDto.from_domain(dish.value)