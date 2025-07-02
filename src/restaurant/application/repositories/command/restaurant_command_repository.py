from abc import ABC, abstractmethod
from src.common.utils import Result
from src.restaurant.domain.aggregate.restaurant import Restaurant

class IRestaurantCommandRepository(ABC):
    @abstractmethod
    async def save(self, restaurant: Restaurant) -> Result[Restaurant]:
        pass
    
    @abstractmethod
    async def delete(self, restaurant: Restaurant) -> Result[Restaurant]:
        pass