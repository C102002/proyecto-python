from fastapi import FastAPI, Depends, status
from typing import List
from src.menu.application.dtos.response.dish_response_dto import DishResponseDto
from src.menu.application.services.get_dishes_by_restaurant_service import GetDishesByRestaurantService
from src.common.application import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from ...routers.menu_router import menu_router
from sqlalchemy.ext.asyncio import AsyncSession
from ...repositories.command.orm_menu_command_repository import OrmMenuCommandRepository
from ...repositories.query.orm_menu_query_repository import OrmMenuQueryRepository
from src.common.infrastructure import GetPostgresqlSession

class GetDishesByRestaurantController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(menu_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        orm_menu_query_repository = OrmMenuQueryRepository(postgres_session)
        orm_menu_command_repository = OrmMenuCommandRepository(postgres_session)

        get_dishes_by_restaurant_service = GetDishesByRestaurantService(
            orm_menu_command_repository,
            orm_menu_query_repository
        )

        return get_dishes_by_restaurant_service

    def setup_routes(self):
        @menu_router.get(
            "/dishes/{restaurant_id}",
            response_model=List[DishResponseDto],
            status_code=status.HTTP_200_OK,
            summary="Get dishes by restaurant",
        )
        async def get_dishes_by_restaurant(restaurant_id: str, menu_service: GetDishesByRestaurantService = Depends(self.get_service)):

            service = ExceptionDecorator(menu_service, FastApiErrorHandler())
            menu = await service.execute(restaurant_id)
            if not menu.value:
                return []
            return [DishResponseDto.from_domain(dish) for dish in menu.value.dishes]
