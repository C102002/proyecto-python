from src.common.application import IService
from src.common.utils.result import Result
from src.dashboard.application.dtos.request.get_reservation_count_request_dto import GetReservationCountRequestDTO
from src.dashboard.application.dtos.response.get_reservation_count_response_dto import GetReservationCountResponseDTO
from src.dashboard.application.repositories.query.dashboard_query_repository import IDashboardQueryRepository


class GetReservationCountService(
    IService[GetReservationCountRequestDTO, GetReservationCountResponseDTO]
):
    """
    Service to fetch the total number of reservations grouped by the specified period.
    """

    def __init__(self, dashboard_query_repository: IDashboardQueryRepository):
        super().__init__()
        self.dashboard_query_repository = dashboard_query_repository

    async def execute(
        self, value: GetReservationCountRequestDTO
    ) -> Result[GetReservationCountResponseDTO]:
        """
        Retrieve reservation count via the dashboard repository.
        """
        result = await self.dashboard_query_repository.get_reservations_count(dto=value)

        if result.is_error:
            return Result.fail(result.error)

        return Result.success(result.value)
