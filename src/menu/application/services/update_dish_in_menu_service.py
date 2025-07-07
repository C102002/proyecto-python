from src.common.utils import Result
from src.menu.application.dtos.request.update_dish_request_dto import UpdateDishRequestDto
from src.menu.application.repositories.command.menu_command_repository import MenuCommandRepository
from src.menu.application.repositories.query.menu_query_repository import MenuQueryRepository
from src.menu.domain.entities.dish import Dish
from src.menu.domain.value_objects.dish_category_vo import DishCategoryVo
from src.menu.domain.value_objects.dish_description_vo import DishDescriptionVo
from src.menu.domain.value_objects.dish_id_vo import DishIdVo
from src.menu.domain.value_objects.dish_image_vo import DishImageVo
from src.menu.domain.value_objects.dish_name_vo import DishNameVo
from src.menu.domain.value_objects.dish_price_vo import DishPriceVo
from src.common.application import IService, ApplicationException

class UpdateDishInMenuService(IService[UpdateDishRequestDto, Dish]):

    def __init__(self, menu_command_repository: MenuCommandRepository, menu_query_repository: MenuQueryRepository):
        self.menu_command_repository = menu_command_repository
        self.menu_query_repository = menu_query_repository
    
    async def execute(self, value: UpdateDishRequestDto) -> Result[Dish]:
        dish_id_vo = DishIdVo(value.dish_id)
        menu = self.menu_query_repository.find_by_dish_id(dish_id_vo)
        if not menu:
            return Result.fail(ApplicationException("Menu not found for the given dish"))

        dish_to_update = None
        for dish in menu.dishes:
            if str(dish.id.value) == value.dish_id:
                dish_to_update = dish
                break

        if not dish_to_update:
            return Result.fail(ApplicationException("Dish not found"))

        if value.name:
            dish_to_update.update_name(DishNameVo(value.name))
        if value.description:
            dish_to_update.update_description(DishDescriptionVo(value.description))
        if value.price:
            dish_to_update.update_price(DishPriceVo(value.price))
        if value.category:
            dish_to_update.update_category(DishCategoryVo(value.category))
        if value.image:
            dish_to_update.update_image(DishImageVo(value.image))

        menu.update_dish(dish_to_update)
        await self.menu_command_repository.update(menu)
        return Result.success(dish_to_update)