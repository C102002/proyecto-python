from typing import List

from src.common.application import IService
from src.common.utils.result import Result
from src.dashboard.application.dtos.request.get_occupacy_percentage_request_dto import GetOccupancyPercentageRequestDto
from src.dashboard.application.dtos.response.get_occupacy_percentage_response_dto import GetOccupancyPercentageResponseDto
from src.dashboard.application.repositories.query.dashboard_query_repository import IDashboardQueryRepository


class GetOccupancyPercentageService(
    IService[GetOccupancyPercentageRequestDto, List[GetOccupancyPercentageResponseDto]]
):
    """
    Service to fetch the occupancy percentage per restaurant 
    for a given period.
    """

    def __init__(self, dashboard_query_repository: IDashboardQueryRepository):
        super().__init__()
        self.dashboard_query_repository = dashboard_query_repository

    async def execute(
        self, value: GetOccupancyPercentageRequestDto
    ) -> Result[List[GetOccupancyPercentageResponseDto]]:
        """
        Retrieve occupancy percentages via the dashboard repository.
        """
        occupancies = await self.dashboard_query_repository.get_occupancy_percentage_by_restaurant(
            dto=value
        )

        if occupancies.is_error:
            return Result.fail(occupancies.fail)

        return Result.success(occupancies)
