from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.cancel_reservation_request_dto import CancelReservationRequest
from src.reservation.application.dtos.response.cancel_reservation_response_dto import CancelReservationResponse
from src.reservation.application.repositories.command.reservation_command_repository import IReservationCommandRepository
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository

class CancelReservationService(IService[CancelReservationRequest, CancelReservationResponse]):

    def __init__(
        self,    
        query_reser: IReservationQueryRepository, 
        command_reser: IReservationCommandRepository,
        ):
        super().__init__()
        self.query_repository = query_reser
        self.command_repository = command_reser
        
    async def execute(self, value: CancelReservationRequest) -> Result[CancelReservationResponse]:
        
        # CLiente no puede cancelar 1 hora antes
        # ADmin puede cancelar cuando quiera
        # UN cliente un puede cancelar una reserva que ya paso
        
        response = CancelReservationResponse()
        return Result.success(response)

