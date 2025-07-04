from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.admin_cancel_reservation_request_dto import AdminCancelReservationRequest
from src.reservation.application.dtos.response.admin_cancel_reservation_response_dto import AdminCancelReservationResponse

class AdminCancelReservationService(IService[AdminCancelReservationRequest, AdminCancelReservationResponse]):

    def __init__(self):
        super().__init__()
        
    async def execute(self, value: AdminCancelReservationRequest) -> Result[AdminCancelReservationResponse]:
        
        # CLiente no puede cancelar 1 hora antes
        # ADmin puede cancelar cuando quiera
        # UN cliente un puede cancelar una reserva que ya paso
        
        response = AdminCancelReservationResponse()
        return Result.success(response)

