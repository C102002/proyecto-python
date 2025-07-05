from typing import List
from src.common.application import IService
from src.common.utils import Result
from src.restaurant.application.dtos.response.create_table_response_dto import CreateTableResponseDTO
from src.restaurant.application.repositories.command.restaurant_command_repository import IRestaurantCommandRepository
from src.restaurant.application.repositories.query.restaurant_query_repository import IRestaurantQueryRepository
from src.restaurant.domain.entities.value_objects.table_number_id_vo import TableNumberId
from ..dtos.request.delete_table_by_id_request_dto import DeleteTableByIdRequestDTO
from ..dtos.response.delete_table_by_id_response_dto import DeleteTableByIdResponseDTO

class DeleteTableByIdService(IService[DeleteTableByIdRequestDTO, DeleteTableByIdResponseDTO]):

    def __init__(self, restaurant_query_repository: IRestaurantQueryRepository,
                 restaurant_command_repository: IRestaurantCommandRepository):
        super().__init__()
        self.restaurant_query_repository = restaurant_query_repository
        self.restaurant_command_repository = restaurant_command_repository

    async def execute(self, value: DeleteTableByIdRequestDTO) -> Result[DeleteTableByIdResponseDTO]:
        
        
        response_repo=await self.restaurant_query_repository.get_by_id(restaurant_id=value.restaurant_id)
        
        if response_repo.is_error:
            return Result.fail(response_repo.error)
        
        table_id=TableNumberId(value.table_id)
        
        restaurant = response_repo.value
        
        restaurant.delete_table(table_id=table_id)
        
        response_delete_repo=await self.restaurant_command_repository.delete_table(data=value)
        
        if response_delete_repo.is_error:
            return Result.fail(response_delete_repo.error)
                
        return Result.success(
            DeleteTableByIdResponseDTO(
                restaurant_id=value.restaurant_id,
                table_id=value.table_id
            )
        )

