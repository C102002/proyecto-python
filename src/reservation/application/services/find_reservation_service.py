from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.find_reservation_request_dto import FindReservationRequest
from src.reservation.application.dtos.response.find_reservation_response_dto import FindReservationResponse

class FindReservationService(IService[FindReservationRequest, FindReservationResponse]):

    def __init__(self):
        super().__init__()
        
    async def execute(self, value: FindReservationRequest) -> Result[FindReservationResponse]:
        
        response = FindReservationResponse()
        return Result.success(response)

