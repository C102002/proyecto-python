from src.menu.application.repositories.query.menu_query_repository import MenuQueryRepository
from src.menu.domain.aggregate.menu import Menu
from src.menu.domain.value_objects.dish_id_vo import DishIdVo
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo

class MenuQueryRepositoryMock(MenuQueryRepository):

    def __init__(self, menu_store: list[Menu]) -> None:
        self.menu_store = menu_store
    
    async def find_by_dish_id(self, dish_id_vo: DishIdVo) -> Menu | None:
        for menu in self.menu_store:
            for dish in menu.dishes:
                if dish.id.value == dish_id_vo.value:
                    return menu
        return None
    
    async def find_by_restaurant_id(self, restaurant_id: RestaurantIdVo) -> Menu | None:
        for menu in self.menu_store:
            if menu.restaurant_id.restaurant_id == restaurant_id.restaurant_id:
                return menu
        
        return None