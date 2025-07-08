from src.common.application import IService, ApplicationException
from src.common.utils import Result
from src.menu.domain.aggregate.menu import Menu
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo
from ..repositories.command.menu_command_repository import MenuCommandRepository
from ..repositories.query.menu_query_repository import MenuQueryRepository

class GetDishesByRestaurantService(IService[str, Menu]):

    def __init__(self, menu_command_repository: MenuCommandRepository, menu_query_repository: MenuQueryRepository):
        self.menu_command_repository = menu_command_repository
        self.menu_query_repository = menu_query_repository
    
    async def execute(self, value: str) -> Result[Menu]:
        restaurant_id_vo = RestaurantIdVo(value)
        menu = await self.menu_query_repository.find_by_restaurant_id(restaurant_id_vo)

        if menu is None:
            return Result.fail(ApplicationException("Menu not found"))

        return Result.success(menu)