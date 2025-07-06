from src.common.utils import Result
from src.common.application import IService

from src.restaurant.application.dtos.request.update_table_request_dto import UpdateTableRequestDTO
from src.restaurant.application.dtos.response.update_table_response_dto import UpdateTableResponseDTO

from src.restaurant.application.repositories.query.restaurant_query_repository import IRestaurantQueryRepository
from src.restaurant.application.repositories.command.restaurant_command_repository import IRestaurantCommandRepository

from src.restaurant.domain.entities.value_objects.table_number_id_vo import TableNumberId
from src.restaurant.domain.entities.value_objects.table_capacity_vo import TableCapacityVo
from src.restaurant.domain.entities.value_objects.table_location_vo import TableLocationVo


class UpdateTableService(IService[UpdateTableRequestDTO, UpdateTableResponseDTO]):

    def __init__(
        self,
        restaurant_query_repository: IRestaurantQueryRepository,
        restaurant_command_repository: IRestaurantCommandRepository
    ):
        super().__init__()
        self.restaurant_query_repository = restaurant_query_repository
        self.restaurant_command_repository   = restaurant_command_repository

    async def execute(
        self,
        dto: UpdateTableRequestDTO
    ) -> Result[UpdateTableResponseDTO]:

        rest_res = await self.restaurant_query_repository.get_by_id(
            restaurant_id=dto.restaurant_id
        )

        if rest_res.is_error:
            return Result.fail(rest_res.error)

        restaurant = rest_res.value

        table_changed = None
        old_id_vo = TableNumberId(dto.number)

        if dto.capacity is not None:
            table_changed = restaurant.update_table_capacity(
                old_id_vo, TableCapacityVo(dto.capacity)
            )

        if dto.location is not None:
            table_changed = restaurant.update_table_location(
                old_id_vo, TableLocationVo(dto.location)
            )

        if dto.new_number is not None:
            # renumera al final, usando todavía el old_id_vo para encontrarla
            table_changed = restaurant.update_table_number(
                old_id_vo, TableNumberId(dto.new_number)
            )



        cmd_res = await self.restaurant_command_repository.update_table(restaurant=restaurant,
                                                                        table=table_changed,
                                                                        old_id=TableNumberId(dto.number))
        
        if cmd_res.is_error:
            return Result.fail(cmd_res.error)

        resp = UpdateTableResponseDTO(
            restaurant_id=restaurant.id.restaurant_id,
            id=table_changed.id.table_number_id,
            capacity=table_changed.capacity.capacity,
            location=table_changed.location.location
        )
        return Result.success(resp)
