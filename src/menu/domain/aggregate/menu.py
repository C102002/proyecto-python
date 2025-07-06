from typing import List
from src.common.domain.aggregate.aggregate_root import AggregateRoot
from src.menu.domain.entities.dish import Dish
from src.menu.domain.value_objects.menu_id_vo import MenuIdVo
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo
from src.menu.domain.domain_exceptions.dish_already_exists_exception import DishAlreadyExistsException
from src.menu.domain.domain_exceptions.dish_not_found_exception import DishNotFoundException

class Menu(AggregateRoot[MenuIdVo]):
    def __init__(self, id: MenuIdVo, restaurant_id: RestaurantIdVo, dishes: List[Dish] = [], categories: List[str] = []):
        super().__init__(id)
        self.restaurant_id = restaurant_id
        self.dishes = dishes
        self.categories = categories

    def add_dish(self, dish: Dish):
        for existing_dish in self.dishes:
            if existing_dish.name.equals(dish.name):
                raise DishAlreadyExistsException(dish.name.value)
        self.dishes.append(dish)

    def update_dish(self, dish_to_update: Dish):
        for i, dish in enumerate(self.dishes):
            if dish.id.equals(dish_to_update.id):
                self.dishes[i] = dish_to_update
                return
        raise DishNotFoundException(dish_to_update.id.value)

    def remove_dish(self, dish_id: str, has_preorders: bool):
        for i, dish in enumerate(self.dishes):
            if dish.id.value == dish_id:
                if has_preorders:
                    dish.set_unavailable()
                else:
                    self.dishes.pop(i)
                return
        raise DishNotFoundException(dish_id)

    def add_category(self, category: str):
        if category not in self.categories:
            self.categories.append(category)

    def remove_category(self, category: str):
        if category in self.categories:
            self.categories.remove(category)
