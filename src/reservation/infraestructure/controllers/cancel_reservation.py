from fastapi import FastAPI, Depends, Security, status, APIRouter
from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession
from src.reservation.application.dtos.request.cancel_reservation_request_dto import CancelReservationRequest
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.reservation.application.services.cancel_reservation_service import CancelReservationService
from src.reservation.infraestructure.dtos.cancel_reservation_inf_request_dto import CancelReservationInfRequestDto
from src.reservation.infraestructure.repositories.command.orm_reservation_command_repository import OrmReservationCommandRepository
from src.reservation.infraestructure.repositories.query.orm_reservation_query_repository import OrmReservationQueryRepository

reservation_router = APIRouter(
    prefix="/reservation",
    tags=["Reservation"],
)
class CancelReservationController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(reservation_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        query_repository = OrmReservationQueryRepository(postgres_session)
        command_repository = OrmReservationCommandRepository(postgres_session)
        service = CancelReservationService(
            query_reser=query_repository,
            command_reser=command_repository,
        )
        return service

    def setup_routes(self):
        @reservation_router.post(
            "/cancel",
            response_model=None,
            status_code=status.HTTP_200_OK,
            summary="Cancelar una reservacion",
            description=("Cancelar una reservacion"),
            response_description="Devuelve 201"
        )
        async def cancel(
            entry: CancelReservationInfRequestDto, 
            service: CancelReservationService = Depends(self.get_service),
            token = Security(UserRoleVerify(), scopes=["client:cancel_reservation"])
            ):
            if service is None:
                raise RuntimeError("CancelReservationService not initialized. Did you forget to call init()?")
            service = ExceptionDecorator(service, FastApiErrorHandler())
            r=await service.execute(
                CancelReservationRequest(
                    reservation_id = entry.reservation_id,
                    client_id = token["user_id"]
                )
            )
            print(f"result cancel: {r}")
            
            return None