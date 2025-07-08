from src.common.utils import Result
from src.restaurant.application.dtos.request.get_all_restaurant_request_dto import GetAllRestaurantRequestDTO
from src.restaurant.application.repositories.query.restaurant_query_repository import IRestaurantQueryRepository
from src.restaurant.domain.aggregate.restaurant import Restaurant
from src.common.infrastructure import InfrastructureException, ExceptionInfrastructureType


class RestaurantQueryRepositoryMock(IRestaurantQueryRepository):

    def __init__(self, restaurant_store: list[Restaurant]) -> None:
        self.restaurant_store = restaurant_store

    async def get_by_id(self, restaurant_id: str) -> Result[Restaurant]:
        restaurant = next((r for r in self.restaurant_store if r.id.restaurant_id == restaurant_id), None)
        if restaurant:
            return Result.success(restaurant)
        return Result.fail(InfrastructureException("Restaurant not found",ExceptionInfrastructureType.NOT_FOUND))
    
    async def get_all_restaurants(self, dto: GetAllRestaurantRequestDTO) -> Result[list[Restaurant]]:
        return Result.success(self.restaurant_store[dto.offset : dto.offset + dto.limit])