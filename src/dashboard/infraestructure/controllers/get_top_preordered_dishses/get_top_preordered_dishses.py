from typing import List

from fastapi import Depends, FastAPI, Security, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.dashboard.application.services.get_top_preordered_dishses_service import GetTopPreorderedDishesService
from src.dashboard.infraestructure.dtos.request.get_top_dishes_preorder_request_dto import GetTopDishesPreorderRequestInfDTO
from src.dashboard.infraestructure.dtos.response.get_occupacy_percentage_response_inf_dto import GetOccupancyPercentageResponseInfDTO
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
            "/dishes/top-preordered",
            response_model=List[GetOccupancyPercentageResponseInfDTO],
            status_code=status.HTTP_200_OK,
            summary="Get top pre-ordered dishes",
            description="Returns the most pre-ordered dishes, limited by top_n",
            response_description="List of dishes with preorder counts"
        )
        async def get_top_preordered_dishes(
            input_dto: GetTopDishesPreorderRequestInfDTO = Depends(),
            service: GetTopPreorderedDishesService = Depends(self.get_query_service),
            token = Security(UserRoleVerify(), scopes=["admin:manage"])
        ):
            decorated = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )
            result = await decorated.execute(input_dto)
            dishes = result.value

            return [
                GetOccupancyPercentageResponseInfDTO(
                    dish_id=dish.dish_id,
                    dish_name=dish.dish_name,
                    total_preorders=dish.total_preorders,
                )
                for dish in dishes
            ]
