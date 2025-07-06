from typing import Optional
from datetime import time

from src.common.utils import Result
from src.common.application import IService

from src.restaurant.application.dtos.request.update_restaurant_request_dto import UpdateRestaurantRequestDTO
from src.restaurant.application.dtos.response.update_restaurant_response_dto import UpdateRestaurantResponseDTO

from src.restaurant.application.repositories.query.restaurant_query_repository import IRestaurantQueryRepository
from src.restaurant.application.repositories.command.restaurant_command_repository import IRestaurantCommandRepository

from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo
from src.restaurant.domain.value_objects.restaurant_name_vo import RestaurantNameVo
from src.restaurant.domain.value_objects.restaurant_location_vo import RestaurantLocationVo
from src.restaurant.domain.value_objects.restaurant_opening_time_vo import RestaurantOpeningTimeVo
from src.restaurant.domain.value_objects.restaurant_closing_time_vo import RestaurantClosingTimeVo


class UpdateRestaurantService(
    IService[UpdateRestaurantRequestDTO, UpdateRestaurantResponseDTO]
):
    def __init__(
        self,
        restaurant_query_repository: IRestaurantQueryRepository,
        restaurant_command_repository: IRestaurantCommandRepository
    ):
        super().__init__()
        self.restaurant_query_repository = restaurant_query_repository
        self.restaurant_command_repository = restaurant_command_repository

    async def execute(
        self,
        dto: UpdateRestaurantRequestDTO
    ) -> Result[UpdateRestaurantResponseDTO]:

        repo_result = await self.restaurant_query_repository.get_by_id(
            restaurant_id=dto.id
        )
        if repo_result.is_error:
            return Result.fail(repo_result.error)

        restaurant = repo_result.value

        if dto.name is not None:
            restaurant.update_name(RestaurantNameVo(dto.name))

        if dto.lat is not None or dto.lng is not None:
            new_lat = dto.lat if dto.lat is not None else restaurant.location.lat
            new_lng = dto.lng if dto.lng is not None else restaurant.location.lng
            restaurant.update_location(RestaurantLocationVo(new_lat, new_lng))

        if dto.opening_time is not None:
            restaurant.update_opening_time(RestaurantOpeningTimeVo(dto.opening_time))

        if dto.closing_time is not None:
            restaurant.update_closing_time(RestaurantClosingTimeVo(dto.closing_time))

        cmd_result = await self.restaurant_command_repository.update_restaurant(
            restaurant=restaurant
        )
        if cmd_result.is_error:
            return Result.fail(cmd_result.error)

        updated = restaurant
        response = UpdateRestaurantResponseDTO(
            id=updated.id.restaurant_id,
            lat=updated.location.lat,
            lng=updated.location.lng,
            name=updated.name.name,
            opening_time=updated.opening_time.opening_time,
            closing_time=updated.closing_time.closing_time,
        )
        return Result.success(response)
