from abc import ABC, abstractmethod
from src.common.utils import Result
from src.restaurant.domain.aggregate.restaurant import Restaurant

class IRestaurantQueryRepository(ABC):
    @abstractmethod
    async def get_by_id(self, restaurant_id: str) -> Result[Restaurant]:
        pass

    @abstractmethod
    async def get_all_restaurants(self) -> Result[list[Restaurant]]:
        pass
    