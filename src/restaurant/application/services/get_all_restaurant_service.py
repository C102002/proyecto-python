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
from ..dtos.request.get_all_restaurant_request_dto import GetAllRestaurantRequestDTO
from ..dtos.response.get_all_restaurant_response_dto import GetAllRestaurantResponseDTO

class GetAllRestaurantService(IService[GetAllRestaurantRequestDTO, List[GetAllRestaurantResponseDTO]]):

    def __init__(self, restaurant_query_repository: IRestaurantQueryRepository):
        super().__init__()
        self.restaurant_query_repository = restaurant_query_repository

    async def execute(self, value: GetAllRestaurantRequestDTO) -> Result[List[GetAllRestaurantResponseDTO]]:
        
        
        response_repo=await self.restaurant_query_repository.get_all_restaurants(dto=value)
        
        if response_repo.is_error:
            return Result.fail(response_repo.error)
        
        restaurants=response_repo.value
        
        return Result.success([
            GetAllRestaurantResponseDTO(
                id=rest.id.restaurant_id,
                lat=rest.location.lat,
                lng=rest.location.lng,
                name=rest.name.name,
                opening_time=rest.opening_time.opening_time,
                closing_time=rest.closing_time.closing_time,
            )
            for rest in restaurants
        ])
        

