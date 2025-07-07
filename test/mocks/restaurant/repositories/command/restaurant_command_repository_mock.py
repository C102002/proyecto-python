from src.common.utils import Result
from src.restaurant.application.dtos.request.delete_table_by_id_request_dto import DeleteTableByIdRequestDTO
from src.restaurant.application.dtos.request.get_all_restaurant_request_dto import GetAllRestaurantRequestDTO
from src.restaurant.application.repositories.command.restaurant_command_repository import IRestaurantCommandRepository
from src.restaurant.domain.aggregate.restaurant import Restaurant
from src.common.infrastructure import InfrastructureException, ExceptionInfrastructureType
from src.restaurant.domain.entities.table import Table
from src.restaurant.domain.entities.value_objects.table_number_id_vo import TableNumberId


class RestaurantCommandRepositoryMock(IRestaurantCommandRepository):

    def __init__(self, restaurant_store: list[Restaurant]) -> None:
        self.restaurant_store = restaurant_store

    async def save(self, restaurant: Restaurant) -> Result[Restaurant]:
        self.restaurant_store.append(restaurant)
        return Result.success(restaurant)
    
    async def delete(self, restaurant: Restaurant) -> Result[Restaurant]:
        self.restaurant_store = [r for r in self.restaurant_store if r.id.restaurant_id != restaurant.id.restaurant_id]
        return Result.success(restaurant)
    
    async def delete_table(self, data: DeleteTableByIdRequestDTO) -> Result[DeleteTableByIdRequestDTO]:
        restaurant = next((r for r in self.restaurant_store if r.id.restaurant_id == data.restaurant_id), None)
        
        if restaurant is None:
            return Result.fail(InfrastructureException("Restaurant not found",ExceptionInfrastructureType.NOT_FOUND))
        
        table  = next((t for t in restaurant.tables if t.id.table_number_id == data.table_id), None)

        if restaurant is None:
            return Result.fail(InfrastructureException("Table not found",ExceptionInfrastructureType.NOT_FOUND))
        
        restaurant.delete_table(TableNumberId(data.table_id))

        return Result.success(data)
    
    async def update_restaurant(self, restaurant: Restaurant) -> Result[Restaurant]:

        for i, r in enumerate(self.restaurant_store):
            if r.id.restaurant_id == restaurant.id.restaurant_id:
                self.restaurant_store[i] = restaurant
                return Result.success(restaurant)
        
        return Result.fail(InfrastructureException("Restaurant not found",ExceptionInfrastructureType.NOT_FOUND))
    
    async def update_table(self, restaurant: Restaurant, table: Table, old_id: TableNumberId) -> Result[Restaurant]:
        
        for r in self.restaurant_store:
            if r.id.restaurant_id == restaurant.id.restaurant_id:
                
                for t in r.tables:
                    if t.id.table_number_id == old_id.table_number_id:
                        r.delete_table(old_id)
                        r.add_table(table)

                        return Result.success(r)
                    
                return Result.fail(InfrastructureException("Table not found",ExceptionInfrastructureType.NOT_FOUND))
            
        return Result.fail(InfrastructureException("Restaurant not found",ExceptionInfrastructureType.NOT_FOUND))
    
    async def add_table(self, restaurant: Restaurant, table: Table) -> Result[Restaurant]:
        restaurant_finded = next((r for r in self.restaurant_store if r.id.restaurant_id == restaurant.id.restaurant_id), None)

        if restaurant_finded is None:
            return Result.fail(InfrastructureException("Restaurant not found",ExceptionInfrastructureType.NOT_FOUND))

        restaurant_finded.add_table(table)
        return Result.success(restaurant_finded)
