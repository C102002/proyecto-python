from fastapi import FastAPI, Depends, status, Security
from src.menu.application.services.remove_dish_from_menu_service import RemoveDishFromMenuService
from src.common.application import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from ...routers.menu_router import menu_router
from sqlalchemy.ext.asyncio import AsyncSession
from ...repositories.command.orm_menu_command_repository import OrmMenuCommandRepository
from ...repositories.query.orm_menu_query_repository import OrmMenuQueryRepository
from src.common.infrastructure import GetPostgresqlSession
from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify

class RemoveDishFromMenuController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(menu_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        orm_menu_query_repository = OrmMenuQueryRepository(postgres_session)
        orm_menu_command_repository = OrmMenuCommandRepository(postgres_session)

        remove_dish_from_menu_service = RemoveDishFromMenuService(
            orm_menu_command_repository,
            orm_menu_query_repository
        )

        return remove_dish_from_menu_service

    def setup_routes(self):
        @menu_router.delete(
            "/dishes/{dish_id}",
            response_model=None,
            status_code=status.HTTP_204_NO_CONTENT,
            summary="Remove dish from menu",
        )
        async def remove_dish_from_menu(dish_id: str, token = Security(UserRoleVerify(), scopes=["admin:manage"]), menu_service: RemoveDishFromMenuService = Depends(self.get_service)):

            service = ExceptionDecorator(menu_service, FastApiErrorHandler())
            await service.execute(dish_id)
