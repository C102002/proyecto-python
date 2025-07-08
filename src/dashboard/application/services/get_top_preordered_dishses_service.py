from typing import List

from src.common.application import IService
from src.common.utils.result import Result
from src.dashboard.application.dtos.request.get_top_dishes_preorder_request_dto import GetTopDishesPreorderRequestDTO
from src.dashboard.application.repositories.query.dashboard_query_repository import GetTopDishesPreorderRequestDTO, IDashboardQueryRepository


class GetTopPreorderedDishesService(
    IService[GetTopDishesPreorderRequestDTO, List[GetTopDishesPreorderRequestDTO]]
):
    """
    Service to fetch the most pre-ordered dishes.
    """

    def __init__(self, dashboard_query_repository: IDashboardQueryRepository):
        super().__init__()
        self.dashboard_query_repository = dashboard_query_repository

    async def execute(
        self, value: GetTopDishesPreorderRequestDTO
    ) -> Result[List[GetTopDishesPreorderRequestDTO]]:
        """
        Fetch the top N pre-ordered dishes via the dashboard repository.
        """
        dishes = await self.dashboard_query_repository.get_top_preordered_dishes(
            dto=value
        )
        
        if dishes.is_error:
            return Result.fail(dishes.fail)

        return Result.success(dishes)
