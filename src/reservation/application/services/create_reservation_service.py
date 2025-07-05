from src.common.application import IService
from src.common.application.id_generator.id_generator import IIdGenerator
from src.common.utils import Result
from src.reservation.application.dtos.request.create_reservation_request_dto import CreateReservationRequest
from src.reservation.application.dtos.response.create_reservation_response_dto import CreateReservationResponse
from src.reservation.application.repositories.command.reservation_command_repository import IReservationCommandRepository
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository

class CreateReservationService(IService[CreateReservationRequest, CreateReservationResponse]):

    def __init__(
        self,    
        query_repository: IReservationQueryRepository, 
        command_repository: IReservationCommandRepository,
        id_generator: IIdGenerator
        ):
        super().__init__()
        self.query_repository = query_repository
        self.command_repository = command_repository
        self.id_generator = id_generator
        
    async def execute(self, value: CreateReservationRequest) -> Result[CreateReservationResponse]:
        
        # CLiente no puede tener mas de 1 reserva activa en el mismo horario
        # LA mesa debe estar disponible en el horario solicitado
        # HOrario de reserva debe estar dentro del horario de apertura, cierre del restarurante
        # MAximo cuatro horas por reserva
        
        
        # NO pueden haber mas de dos reservas activas para la misma mesa en el mismo horario
        # UN cliente no puede tener dos reservas en el mismo horario, incluso en diferentes restaurantes
        # Los platos deben pertenecer al menu udel restaurante de la mesa reservada
        
        
        response = CreateReservationResponse()
        return Result.success(response)

