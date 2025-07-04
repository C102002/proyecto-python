from typing import List
from src.common.application import IService
from src.common.application.id_generator.id_generator import IIdGenerator
from src.common.utils import Result
from src.restaurant.application.dtos.response.create_table_response_dto import CreateTableResponseDTO
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
from ..dtos.request.create_restaurant_request_dto import CreateRestaurantRequestDTO
from ..dtos.response.create_restaurant_response_dto import CreateRestaurantResponseDTO
from ..repositories.command.restaurant_command_repository import IRestaurantCommandRepository

class CreateRestaurantService(IService[CreateRestaurantRequestDTO, CreateRestaurantResponseDTO]):

    def __init__(self, restaurant_command_repository: IRestaurantCommandRepository, id_generator:IIdGenerator,tables_id_generator:IIdGenerator):
        super().__init__()
        self.restaurant_command_repository = restaurant_command_repository
        self.id_generator = id_generator
        self.tables_id_generator = tables_id_generator

    async def execute(self, value: CreateRestaurantRequestDTO) -> Result[CreateRestaurantResponseDTO]:
        
        domain_tables: List[Table] = []
        for tbl_dto in value.tables or []:
            table_id = TableNumberId(int(self.tables_id_generator.generate_id()))
            capacity = TableCapacityVo(tbl_dto.capacity)
            location = TableLocationVo(tbl_dto.location)
            domain_tables.append(Table(id=table_id,capacity=capacity,location=location))
        
        print(domain_tables)
        
        restaurant=Restaurant(
            RestaurantIdVo(self.id_generator.generate_id()),
            RestaurantNameVo(value.name),
            RestaurantLocationVo(value.lat,value.lng),
            RestaurantOpeningTimeVo(value.opening_time),
            RestaurantClosingTimeVo(value.closing_time),
            tables=domain_tables
        )
        
        response_repo=await self.restaurant_command_repository.save(restaurant=restaurant)
        
        if response_repo.is_error:
            return Result.fail(response_repo.error)
        
        response = CreateRestaurantResponseDTO(
            id=restaurant.id.restaurant_id,
            lat=restaurant.location.lat,
            lng=restaurant.location.lng,
            name=restaurant.name.name,
            opening_time=restaurant.opening_time.opening_time,
            closing_time=restaurant.closing_time.closing_time,
            tables=[
                CreateTableResponseDTO(
                    id=tbl.id.table_number_id,
                    capacity=tbl.capacity.capacity,
                    location=tbl.location.location.value,
                    restaurant_id=restaurant.id.restaurant_id
                )
                for tbl in restaurant.tables
            ]
        )
        
        return Result.success(response)

