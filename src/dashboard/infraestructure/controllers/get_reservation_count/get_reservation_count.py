from fastapi import Depends, FastAPI, Security, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession

from src.dashboard.application.services.get_reservation_count_service import GetReservationCountService
from src.dashboard.infraestructure.dtos.request.get_reservation_count_request_inf_dto import (
    GetReservationCountRequestInfDTO,
)
from src.dashboard.infraestructure.dtos.response.get_reservation_count_response_inf_dto import (
    GetReservationCountResponseInfDTO,
)
from src.dashboard.infraestructure.repositories.query.orm_dashboard_query_repository import OrmDashboardQueryRepository
from src.dashboard.infraestructure.routers.dashboard_router import dashboard_router


class GetReservationCountController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(dashboard_router)

    async def get_query_service(
        self,
        session: AsyncSession = Depends(GetPostgresqlSession()),
    ) -> GetReservationCountService:
        repo = OrmDashboardQueryRepository(session)
        return GetReservationCountService(dashboard_query_repository=repo)

    def setup_routes(self):
        @dashboard_router.get(
            "/reservations/count",
            response_model=GetReservationCountResponseInfDTO,
            status_code=status.HTTP_200_OK,
            summary="Get reservation count",
            description="Returns total number of reservations grouped by DAY or WEEK",
            response_description="Reservation count by period"
        )
        async def get_reservation_count(
            input_dto: GetReservationCountRequestInfDTO = Depends(),
            service: GetReservationCountService = Depends(self.get_query_service),
            token = Security(UserRoleVerify(), scopes=["admin:manage"])
        ):
            decorated = ExceptionDecorator(
                service=service,
                error_handler=FastApiErrorHandler()
            )
            app_dto = input_dto.to_dto()
            result = await decorated.execute(app_dto)
            data = result.value
            
            print(f"llego {data}")

            return GetReservationCountResponseInfDTO(
                period_type=data.period_type,
                count=data.count
            )
