from fastapi import FastAPI, Depends, Security, status, APIRouter
from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession
from src.reservation.application.dtos.request.admin_cancel_reservation_request_dto import AdminCancelReservationRequest
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.reservation.application.services.admin_cancel_reservation_service import AdminCancelReservationService
from src.reservation.application.services.cancel_reservation_service import CancelReservationService
from src.reservation.infraestructure.dtos.admin_cancel_reservation_inf_request_dto import AdminCancelReservationInfRequestDto
from src.reservation.infraestructure.repositories.command.orm_reservation_command_repository import OrmReservationCommandRepository
from src.reservation.infraestructure.repositories.query.orm_reservation_query_repository import OrmReservationQueryRepository

reservation_router = APIRouter(
    prefix="/reservation",
    tags=["Reservation"],
)
class AdminCancelReservationController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(reservation_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        query_repository = OrmReservationQueryRepository(postgres_session)
        command_repository = OrmReservationCommandRepository(postgres_session)
        service = AdminCancelReservationService(
            query_reser=query_repository,
            command_reser=command_repository,
        )
        return service

    def setup_routes(self):
        @reservation_router.post(
            "/admin/cancel",
            response_model=None,
            status_code=status.HTTP_200_OK,
            summary="Cancelar una reservacion",
            description=("Cancelar una reservacion"),
            response_description="Devuelve 201"
        )
        async def cancel(
            entry: AdminCancelReservationInfRequestDto, 
            service: AdminCancelReservationService = Depends(self.get_service),
            token = Security(UserRoleVerify(), scopes=["admin:manage"])
            ):
            if service is None:
                raise RuntimeError("AdminCancelReservationService not initialized. Did you forget to call init()?")
            service = ExceptionDecorator(service, FastApiErrorHandler())
            await service.execute(
                AdminCancelReservationRequest(
                    reservation_id = entry.reservation_id,
                )
            )
            return None