from abc import ABC, abstractmethod
from src.common.utils import Result
from src.restaurant.application.dtos.request.delete_table_by_id_request_dto import DeleteTableByIdRequestDTO
from src.restaurant.domain.aggregate.restaurant import Restaurant
from src.restaurant.domain.entities.table import Table

class IRestaurantCommandRepository(ABC):
    @abstractmethod
    async def save(self, restaurant: Restaurant) -> Result[Restaurant]:
        pass
    
    @abstractmethod
    async def add_table(self, restaurant: Restaurant, table:Table) -> Result[Restaurant]:
        pass
    
    @abstractmethod
    async def delete(self, restaurant: Restaurant) -> Result[Restaurant]:
        pass
    
    @abstractmethod
    async def delete_table(self, data:DeleteTableByIdRequestDTO) -> Result[DeleteTableByIdRequestDTO]:
        pass
    
    @abstractmethod
    async def update_restaurant(self, restaurant: Restaurant) -> Result[Restaurant]:
        pass