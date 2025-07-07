from abc import ABC, abstractmethod
from typing import Optional
from src.menu.domain.aggregate.menu import Menu
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo
from src.menu.domain.value_objects.dish_id_vo import DishIdVo

class MenuQueryRepository(ABC):

    @abstractmethod
    async def find_by_restaurant_id(self, restaurant_id: RestaurantIdVo) -> Optional[Menu]:
        pass

    @abstractmethod
    async def find_by_dish_id(self, dish_id_vo: DishIdVo) -> Optional[Menu]:
        pass
