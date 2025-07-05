from fastapi import FastAPI, Depends, status, APIRouter
from src.common.infrastructure.middlewares.get_postgresql_session import GetPostgresqlSession
from src.reservation.application.dtos.request.create_reservation_request_dto import CreateReservationRequest
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.common.infrastructure.id_generator.uuid_generator import UuidGenerator
from src.reservation.application.services.create_reservation_service import CreateReservationService
from src.reservation.infraestructure.dtos.create_reservation_request import CreateReservationRequestController
from src.reservation.infraestructure.repositories.command.orm_reservation_command_repository import OrmReservationCommandRepository
from src.reservation.infraestructure.repositories.query.orm_reservation_query_repository import OrmReservationQueryRepository

reservation_router = APIRouter(
    prefix="/reservation",
    tags=["Reservation"],
)
class CreateReservationController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(reservation_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        query_repository = OrmReservationQueryRepository(postgres_session)
        command_repository = OrmReservationCommandRepository(postgres_session)
        #query_restau = OrmRestaurantQueryRepository(postgres_session)
        id_generator = UuidGenerator()
        
        service = CreateReservationService(
            query_reser=query_repository,
            command_reser=command_repository,
            id_generator=id_generator,
            #query_restau=query_restau
        )
        return service

    def setup_routes(self):
        @reservation_router.post(
            "/create",
            response_model=None,
            status_code=status.HTTP_200_OK,
            summary="Create a reservation",
            description=("Crea una reservacion"),
            response_description="Devuelve 201"
        )
        async def create(
            entry: CreateReservationRequestController, 
            service: CreateReservationService = Depends(self.get_service)
            ):
            if service is None:
                raise RuntimeError("CreateReservationService not initialized. Did you forget to call init()?")
            service = ExceptionDecorator(service, FastApiErrorHandler())
            await service.execute(
                CreateReservationRequest(
                    client_id=entry.client_id,
                    date_start=entry.date_start,
                    date_end=entry.date_end
                )
            )
            return None