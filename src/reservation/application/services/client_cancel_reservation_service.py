from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.client_cancel_reservation_request_dto import ClientCancelReservationRequest
from src.reservation.application.dtos.response.client_cancel_reservation_response_dto import ClientCancelReservationResponse

class ClientCancelReservationService(IService[ClientCancelReservationRequest, ClientCancelReservationResponse]):

    def __init__(self):
        super().__init__()
        
    async def execute(self, value: ClientCancelReservationRequest) -> Result[ClientCancelReservationResponse]:
        
        # CLiente no puede cancelar 1 hora antes
        # ADmin puede cancelar cuando quiera
        # UN cliente un puede cancelar una reserva que ya paso
        
        response = ClientCancelReservationResponse()
        return Result.success(response)

