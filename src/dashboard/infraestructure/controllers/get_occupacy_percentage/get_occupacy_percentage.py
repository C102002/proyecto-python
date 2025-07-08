from typing import List

from fastapi import Depends, FastAPI, Security, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession


from src.dashboard.application.services.get_occupacy_percentage_service import GetOccupancyPercentageService
from src.dashboard.infraestructure.dtos.request.get_occupacy_percentage_request_inf_dto import GetOccupancyPercentageRequestInfDTO
from src.dashboard.infraestructure.dtos.response.get_occupacy_percentage_response_inf_dto import GetOccupancyPercentageResponseInfDTO
from src.dashboard.infraestructure.repositories.query.orm_dashboard_query_repository import OrmDashboardQueryRepository
from src.dashboard.infraestructure.routers.dashboard_router import dashboard_router


class GetOccupancyPercentageController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(dashboard_router)

    async def get_query_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession()),
    ) -> GetOccupancyPercentageService:
        repo = OrmDashboardQueryRepository(session)
        return GetOccupancyPercentageService(dashboard_query_repository=repo)

    def setup_routes(self):
        @dashboard_router.get(
            "/ocupacion",
            response_model=List[GetOccupancyPercentageResponseInfDTO],
            status_code=status.HTTP_200_OK,
            summary="Get occupancy percentage",
            description="Returns occupancy percentage per restaurant for a given period",
            response_description="List of occupancy percentages"
        )
        async def get_occupancy(
            input_dto: GetOccupancyPercentageRequestInfDTO = Depends(),
            service: GetOccupancyPercentageService = Depends(self.get_query_service),
            token = Security(UserRoleVerify(), scopes=["admin:manage"])
        ):
            decorated = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )
            
            app_dto = input_dto.to_dto()
            result = await decorated.execute(app_dto)
            
            occupancies = result.value

            return [
                GetOccupancyPercentageResponseInfDTO(
                    restaurant_id=occ.restaurant_id,
                    restaurant_name=occ.restaurant_name,
                    occupied_tables=occ.occupied_tables,
                    total_tables=occ.total_tables,
                    occupancy_percent=occ.occupancy_percent,
                )
                for occ in occupancies
            ]
