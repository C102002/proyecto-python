from src.common.utils import Result
from src.menu.application.dtos.request.create_dish_request_dto import CreateDishRequestDto
from src.menu.application.dtos.request.update_dish_request_dto import UpdateDishRequestDto
from src.menu.application.repositories.command.menu_command_repository import MenuCommandRepository
from src.menu.application.repositories.query.menu_query_repository import MenuQueryRepository
from src.menu.domain.aggregate.menu import Menu
from src.menu.domain.entities.dish import Dish
from src.menu.domain.value_objects.dish_category_vo import DishCategoryVo
from src.menu.domain.value_objects.dish_description_vo import DishDescriptionVo
from src.menu.domain.value_objects.dish_id_vo import DishIdVo
from src.menu.domain.value_objects.dish_image_vo import DishImageVo
from src.menu.domain.value_objects.dish_name_vo import DishNameVo
from src.menu.domain.value_objects.dish_price_vo import DishPriceVo
from src.menu.domain.value_objects.menu_id_vo import MenuIdVo
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo
from src.common.application import IService, ApplicationException, ExceptionApplicationType


class AddDishToMenuService(IService[CreateDishRequestDto, Dish]):

    def __init__(self, menu_command_repository: MenuCommandRepository, menu_query_repository: MenuQueryRepository):
        self.menu_command_repository = menu_command_repository
        self.menu_query_repository = menu_query_repository
    
    async def execute(self, value: CreateDishRequestDto) -> Result[Dish]:
        restaurant_id_vo = RestaurantIdVo(value.restaurant_id)
        menu = await self.menu_query_repository.find_by_restaurant_id(restaurant_id_vo)

        if not menu:
            restaurant_id_vo = RestaurantIdVo(value.restaurant_id)
            menu = Menu(MenuIdVo(), restaurant_id_vo)
            await self.menu_command_repository.save(menu)
        else:
            listDishName = [dish.name.value for dish in menu.dishes]

            if (value.name in listDishName):
                return Result.fail(ApplicationException("There is already a dish with that name", ExceptionApplicationType.CONFLICT))

        dish = Dish(
            DishIdVo(),
            DishNameVo(value.name),
            DishDescriptionVo(value.description),
            DishPriceVo(value.price),
            DishCategoryVo(value.category),
            DishImageVo(value.image) if value.image else DishImageVo()
        )
        menu.add_dish(dish)
        await self.menu_command_repository.update(menu)
        return Result.success(dish)