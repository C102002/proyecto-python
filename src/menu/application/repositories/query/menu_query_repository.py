from abc import ABC, abstractmethod
from typing import Optional
from src.menu.domain.aggregate.menu import Menu
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo

class MenuQueryRepository(ABC):

    @abstractmethod
    def find_by_restaurant_id(self, restaurant_id: RestaurantIdVo) -> Optional[Menu]:
        pass
