from typing import List

from fastapi import Depends, FastAPI, Security, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.dashboard.application.services.get_top_preordered_dishses_service import GetTopPreorderedDishesService
from src.dashboard.infraestructure.dtos.request.get_top_dishes_preorder_request_dto import GetTopDishesPreorderRequestInfDTO
from src.dashboard.infraestructure.dtos.response.get_top_dishes_preorder_response_dto import GetTopDishesPreorderResponseInfDTO
from src.dashboard.infraestructure.repositories.query.orm_dashboard_query_repository import OrmDashboardQueryRepository
from src.dashboard.infraestructure.routers.dashboard_router import dashboard_router


class GetTopPreorderedDishesController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(dashboard_router)

    async def get_query_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession()),
    ) -> GetTopPreorderedDishesService:
        repo = OrmDashboardQueryRepository(session)
        return GetTopPreorderedDishesService(dashboard_query_repository=repo)

    def setup_routes(self):
        @dashboard_router.get(
            "/platos",
            response_model=List[GetTopDishesPreorderResponseInfDTO],
            status_code=status.HTTP_200_OK,
            summary="Get top pre-ordered dishes",
            description="Devuelve los platos más pre-ordenados, limitado por top_n",
            response_description="Lista de platos con conteo de pre-órdenes"
        )
        async def get_top_preordered_dishes(
            input_dto: GetTopDishesPreorderRequestInfDTO = Depends(),
            service: GetTopPreorderedDishesService = Depends(self.get_query_service),
            token = Security(UserRoleVerify(), scopes=["admin:manage"])
        ):
            app_dto = input_dto.to_dto()
            decorated = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )
            result = await decorated.execute(app_dto)
            dishes = result.value

            return [
                GetTopDishesPreorderResponseInfDTO(
                    dish_id=dish.dish_id,
                    dish_name=dish.dish_name,
                    total_preorders=dish.total_preorders,
                )
                for dish in dishes
            ]
