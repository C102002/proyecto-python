from abc import ABC, abstractmethod
from src.common.utils import Result
from src.restaurant.application.dtos.request.get_all_restaurant_request_dto import GetAllRestaurantRequestDTO
from src.restaurant.domain.aggregate.restaurant import Restaurant

class IRestaurantQueryRepository(ABC):
    @abstractmethod
    async def get_by_id(self, restaurant_id: str) -> Result[Restaurant]:
        pass

    @abstractmethod
    async def get_all_restaurants(self,dto:GetAllRestaurantRequestDTO) -> Result[list[Restaurant]]:
        pass
    