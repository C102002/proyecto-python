from typing import List
from src.common.application import IService
from src.common.application.id_generator.id_generator import IIdGenerator
from src.common.utils import Result
from src.restaurant.application.dtos.response.create_table_response_dto import CreateTableResponseDTO
from src.restaurant.application.repositories.query.restaurant_query_repository import IRestaurantQueryRepository
from src.restaurant.domain.aggregate.restaurant import Restaurant
from src.restaurant.domain.entities.table import Table
from src.restaurant.domain.entities.value_objects.table_capacity_vo import TableCapacityVo
from src.restaurant.domain.entities.value_objects.table_location_vo import TableLocationVo
from src.restaurant.domain.entities.value_objects.table_number_id_vo import TableNumberId
from src.restaurant.domain.value_objects.restaurant_closing_time_vo import RestaurantClosingTimeVo
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo
from src.restaurant.domain.value_objects.restaurant_location_vo import RestaurantLocationVo
from src.restaurant.domain.value_objects.restaurant_name_vo import RestaurantNameVo
from src.restaurant.domain.value_objects.restaurant_opening_time_vo import RestaurantOpeningTimeVo
from ..dtos.request.create_table_request_dto import CreateTableRequestDTO
from ..dtos.response.create_table_response_dto import CreateTableResponseDTO
from ..repositories.command.restaurant_command_repository import IRestaurantCommandRepository

class CreateTableService(IService[CreateTableRequestDTO, CreateTableResponseDTO]):

    def __init__(self, restaurant_command_repository: IRestaurantCommandRepository,
                 restaurant_query_repository:IRestaurantQueryRepository):
        super().__init__()
        self.restaurant_command_repository = restaurant_command_repository
        self.restaurant_query_repository = restaurant_query_repository

    async def execute(self, value: CreateTableRequestDTO) -> Result[CreateTableResponseDTO]:
        
        restaurant_result = await self.restaurant_query_repository.get_by_id(restaurant_id=value.restaurant_id)
        
        if restaurant_result.is_error:
            return Result.fail(response_repo.error)
        
        restaurant= restaurant_result.value
        
        table = Table(
            TableNumberId(table_number_id=value.number),
            TableLocationVo(location=value.location),
            TableCapacityVo(capacity=value.capacity)
        )
        
        restaurant.add_table(table=table)
        
        response_repo=await self.restaurant_command_repository.add_table(restaurant=restaurant,table=table)
        
        if response_repo.is_error:
            return Result.fail(response_repo.error)
        
        print(f"valor del id {value.number}")
        print(f"valor del id a traves de table {table.id.table_number_id}")
        
        
        response = CreateTableResponseDTO(
            id=table.id.table_number_id,
            restaurant_id=restaurant.id.restaurant_id,
            capacity=table.capacity.capacity,
            location=table.location.location,
        )
        
        return Result.success(response)

