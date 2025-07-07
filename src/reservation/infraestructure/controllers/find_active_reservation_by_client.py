from fastapi import FastAPI, Depends, Path, Security, status, APIRouter
from src.auth.infrastructure.middlewares.user_role_verify import UserRoleVerify
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.reservation.application.dtos.request.find_active_reservation_request_dto import FindActiveReservationRequest
from src.reservation.application.services.find_active_reservation_by_client_id_service import FindActiveReservationByClientService
from src.reservation.infraestructure.repositories.query.orm_reservation_query_repository import OrmReservationQueryRepository

reservation_router = APIRouter(
    prefix="/reservation",
    tags=["Reservation"],
)

class FindActiveReservationController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(reservation_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        query_repository = OrmReservationQueryRepository(postgres_session)
        service = FindActiveReservationByClientService(
            query_reser=query_repository,
        )
        return service

    def setup_routes(self):
        @reservation_router.get(
            "/find-active/{client_id}",
            response_model=None,
            status_code=status.HTTP_200_OK,
            summary="Encontrar reservaciones activaes",
            description=("Encontrar reservaciones activas"),
            response_description="Devuelve una lista de reservaciones"
        )
        async def find(
            client_id: str = Path(..., description="ID del cliente"),
            service: FindActiveReservationByClientService = Depends(self.get_service),
            token = Security(UserRoleVerify(), scopes=["client:view_reservation"])
            ):
            if service is None:
                raise RuntimeError("FindActiveReservationService not initialized. Did you forget to call init()?")
            service = ExceptionDecorator(service, FastApiErrorHandler())
            result = await service.execute(
                FindActiveReservationRequest(
                    client_id=client_id
                )
            )
            return result.value