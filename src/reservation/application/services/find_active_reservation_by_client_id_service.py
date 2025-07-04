from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.find_active_reservation_request_dto import FindActiveReservationRequest
from src.reservation.application.dtos.response.find_active_reservation_response_dto import FindActiveReservationResponse

class FindActiveReservationByClientIDService(IService[FindActiveReservationRequest, FindActiveReservationResponse]):

    def __init__(self):
        super().__init__()
        
    async def execute(self, value: FindActiveReservationRequest) -> Result[FindActiveReservationResponse]:
        
        response = FindActiveReservationResponse()
        return Result.success(response)

