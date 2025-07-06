from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.find_reservation_request_dto import FindReservationRequest
from src.reservation.application.dtos.response.find_reservation_response_dto import FindReservationResponse
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository

class FindReservationService(IService[FindReservationRequest, FindReservationResponse]):

    def __init__(
        self,    
        query_reser: IReservationQueryRepository, 
        ):
        super().__init__()
        self.query_repository = query_reser
        
    async def execute(self, value: FindReservationRequest) -> Result[FindReservationResponse]:
        find = await self.query_repository.get_all()
        response = FindReservationResponse(reservations=find)
        return Result.success(response)

