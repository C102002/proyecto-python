from typing import List
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


class MenuService:

    def __init__(self, menu_command_repository: MenuCommandRepository, menu_query_repository: MenuQueryRepository):
        self.menu_command_repository = menu_command_repository
        self.menu_query_repository = menu_query_repository

    def create_menu(self, restaurant_id: str) -> Menu:
        restaurant_id_vo = RestaurantIdVo(restaurant_id)
        menu = Menu(MenuIdVo(), restaurant_id_vo)
        self.menu_command_repository.save(menu)
        return menu

    def add_dish_to_menu(self, restaurant_id: str, dish_dto: CreateDishRequestDto) -> Dish:
        restaurant_id_vo = RestaurantIdVo(restaurant_id)
        menu = self.menu_query_repository.find_by_restaurant_id(restaurant_id_vo)
        if not menu:
            menu = self.create_menu(restaurant_id)

        dish = Dish(
            DishIdVo(),
            DishNameVo(dish_dto.name),
            DishDescriptionVo(dish_dto.description),
            DishPriceVo(dish_dto.price),
            DishCategoryVo(dish_dto.category),
            DishImageVo(dish_dto.image) if dish_dto.image else None
        )
        menu.add_dish(dish)
        self.menu_command_repository.update(menu)
        return dish

    def update_dish_in_menu(self, dish_id: str, dish_dto: UpdateDishRequestDto) -> Dish:
        dish_id_vo = DishIdVo(dish_id)
        menu = self.menu_query_repository.find_by_dish_id(dish_id_vo)
        if not menu:
            raise Exception("Menu not found for the given dish")

        dish_to_update = None
        for dish in menu.dishes:
            if str(dish.id.value) == dish_id:
                dish_to_update = dish
                break

        if not dish_to_update:
            raise Exception("Dish not found")

        if dish_dto.name:
            dish_to_update.update_name(DishNameVo(dish_dto.name))
        if dish_dto.description:
            dish_to_update.update_description(DishDescriptionVo(dish_dto.description))
        if dish_dto.price:
            dish_to_update.update_price(DishPriceVo(dish_dto.price))
        if dish_dto.category:
            dish_to_update.update_category(DishCategoryVo(dish_dto.category))
        if dish_dto.image:
            dish_to_update.update_image(DishImageVo(dish_dto.image))

        menu.update_dish(dish_to_update)
        self.menu_command_repository.update(menu)
        return dish_to_update

    def remove_dish_from_menu(self, dish_id: str):
        dish_id_vo = DishIdVo(dish_id)
        menu = self.menu_query_repository.find_by_dish_id(dish_id_vo)
        if not menu:
            raise Exception("Menu not found for the given dish")

        # This is a simulation, in a real scenario we would check for pre-orders
        has_preorders = False

        menu.remove_dish(dish_id, has_preorders)
        self.menu_command_repository.update(menu)

    def get_menu_by_restaurant_id(self, restaurant_id: str) -> Menu:
        restaurant_id_vo = RestaurantIdVo(restaurant_id)
        return self.menu_query_repository.find_by_restaurant_id(restaurant_id_vo)
