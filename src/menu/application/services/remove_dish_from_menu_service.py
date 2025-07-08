from src.common.application import IService, ApplicationException
from src.common.utils import Result
from ..repositories.command.menu_command_repository import MenuCommandRepository
from ..repositories.query.menu_query_repository import MenuQueryRepository
from src.menu.domain.value_objects.dish_id_vo import DishIdVo

class RemoveDishFromMenuService(IService[str, None]):

    def __init__(self, menu_command_repository: MenuCommandRepository, menu_query_repository: MenuQueryRepository):
        self.menu_command_repository = menu_command_repository
        self.menu_query_repository = menu_query_repository

    async def execute(self, value: str) -> Result[None]:
        dish_id_vo = DishIdVo(value)
        menu = await self.menu_query_repository.find_by_dish_id(dish_id_vo)
        if not menu:
            return Result.fail(ApplicationException("Menu not found for the given dish"))

        # This is a simulation, in a real scenario we would check for pre-orders
        has_preorders = False

        menu.remove_dish(value, has_preorders)
        await self.menu_command_repository.update(menu)

        return Result.success(None)