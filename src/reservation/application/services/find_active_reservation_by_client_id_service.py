from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.find_active_reservation_request_dto import FindActiveReservationRequest
from src.reservation.application.dtos.response.find_active_reservation_response_dto import FindActiveReservationResponse
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository

class FindActiveReservationByClientService(IService[FindActiveReservationRequest, FindActiveReservationResponse]):

    def __init__(
        self,    
        query_reser: IReservationQueryRepository, 
        ):
        super().__init__()
        self.query_repository = query_reser
    async def execute(self, value: FindActiveReservationRequest) -> Result[FindActiveReservationResponse]:
        find = await self.query_repository.get_active_by_client_id(client_id=value.client_id)
        response = FindActiveReservationResponse(reservations=find)
        return Result.success(response)

