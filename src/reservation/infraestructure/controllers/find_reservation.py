from fastapi import FastAPI, Depends, status, APIRouter
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.reservation.application.dtos.request.find_reservation_request_dto import FindReservationRequest
from src.reservation.application.services.find_reservation_service import FindReservationService
from src.reservation.infraestructure.dtos.find_reservation_request import FindReservationRequestController
from src.reservation.infraestructure.repositories.command.orm_reservation_command_repository import OrmReservationCommandRepository
from src.reservation.infraestructure.repositories.query.orm_reservation_query_repository import OrmReservationQueryRepository

reservation_router = APIRouter(
    prefix="/reservation",
    tags=["Reservation"],
)

class FindReservationController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(reservation_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        query_repository = OrmReservationQueryRepository(postgres_session)
        command_repository = OrmReservationCommandRepository(postgres_session)
        #query_restau = OrmRestaurantQueryRepository(postgres_session)
        service = FindReservationService(
            query_reser=query_repository,
            command_reser=command_repository,
            #query_restau=query_restau
        )
        return service

    def setup_routes(self):
        @reservation_router.get(
            "/find",
            response_model=None,
            status_code=status.HTTP_200_OK,
            summary="Encontrar reservaciones",
            description=("Encontrar reservaciones"),
            response_description="Devuelve una lista de reservaciones"
        )
        async def find(
            entry: FindReservationRequestController, 
            service: FindReservationService = Depends(self.get_service)
            ):
            if service is None:
                raise RuntimeError("FindReservationService not initialized. Did you forget to call init()?")
            service = ExceptionDecorator(service, FastApiErrorHandler())
            await service.execute(
                FindReservationRequest()
            )
            return None