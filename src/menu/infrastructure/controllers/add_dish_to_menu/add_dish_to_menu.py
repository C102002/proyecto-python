from fastapi import FastAPI, Depends, status
from src.menu.application.dtos.request.create_dish_request_dto import CreateDishRequestDto
from ...dtos.request.create_dish_request_inf_dto import CreateDishRequesInftDto
from src.menu.application.dtos.response.dish_response_dto import DishResponseDto
from src.menu.application.services.add_dish_to_menu_service import AddDishToMenuService
from src.menu.infrastructure.dependencies import get_menu_service
from src.common.application import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from ...routers.menu_router import menu_router
from sqlalchemy.ext.asyncio import AsyncSession
from ...repositories.command.orm_menu_command_repository import OrmMenuCommandRepository
from ...repositories.query.orm_menu_query_repository import OrmMenuQueryRepository
from src.common.infrastructure import GetPostgresqlSession

class AddDishToMenuController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(menu_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        orm_menu_query_repository = OrmMenuQueryRepository(postgres_session)
        orm_menu_command_repository = OrmMenuCommandRepository(postgres_session)

        add_dish_to_menu_service = AddDishToMenuService(
            orm_menu_command_repository,
            orm_menu_query_repository
        )

        return add_dish_to_menu_service

    def setup_routes(self):
        @menu_router.post(
            "/dishes/{restaurant_id}",
            response_model=DishResponseDto,
            status_code=status.HTTP_200_OK,
            summary="Add a dish",
        )
        async def add_dish_to_menu(restaurant_id: str, dish_dto: CreateDishRequesInftDto, menu_service: AddDishToMenuService = Depends(self.get_service)):

            request = CreateDishRequestDto(
                name=dish_dto.name,
                restaurant_id=restaurant_id,
                description=dish_dto.description,
                category=dish_dto.category,
                price=dish_dto.price,
                image=dish_dto.image
            )
            service = ExceptionDecorator(menu_service, FastApiErrorHandler())
            dish = await service.execute(request)
            return DishResponseDto.from_domain(dish.value)
