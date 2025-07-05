from typing import List
from src.common.application import IService
from src.common.utils import Result
from src.restaurant.application.dtos.response.create_table_response_dto import CreateTableResponseDTO
from src.restaurant.application.repositories.command.restaurant_command_repository import IRestaurantCommandRepository
from src.restaurant.application.repositories.query.restaurant_query_repository import IRestaurantQueryRepository
from ..dtos.request.delete_restaurant_by_id_request_dto import DeleteRestaurantByIdRequestDTO
from ..dtos.response.delete_restaurant_by_id_response_dto import DeleteRestaurantByIdResponseDTO

class DeleteRestaurantByIdService(IService[DeleteRestaurantByIdRequestDTO, DeleteRestaurantByIdResponseDTO]):

    def __init__(self, restaurant_query_repository: IRestaurantQueryRepository,
                 restaurant_command_repository: IRestaurantCommandRepository):
        super().__init__()
        self.restaurant_query_repository = restaurant_query_repository
        self.restaurant_command_repository = restaurant_command_repository

    async def execute(self, value: DeleteRestaurantByIdRequestDTO) -> Result[DeleteRestaurantByIdResponseDTO]:
        
        
        response_repo=await self.restaurant_query_repository.get_by_id(restaurant_id=value.restaurant_id)
        
        if response_repo.is_error:
            return Result.fail(response_repo.error)
        
        restaurant = response_repo.value
        
        restaurant.delete()
        
        response_delete_repo=await self.restaurant_command_repository.delete(restaurant=restaurant)
        
        if response_delete_repo.is_error:
            return Result.fail(response_delete_repo.error)
                
        return Result.success(
            DeleteRestaurantByIdResponseDTO(
                restaurant_id=value.restaurant_id
            )
        )

