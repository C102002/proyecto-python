from typing import Optional
from sqlalchemy.orm import Session
from src.menu.application.repositories.command.menu_command_repository import MenuCommandRepository
from src.menu.application.repositories.query.menu_query_repository import MenuQueryRepository
from src.menu.domain.aggregate.menu import Menu
from src.menu.infrastructure.models.menu_model import MenuModel, DishModel
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo

class MenuRepository(MenuCommandRepository, MenuQueryRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, menu: Menu) -> None:
        menu_model = MenuModel.from_domain(menu)
        self.session.add(menu_model)

    def update(self, menu: Menu) -> None:
        menu_model = self.session.query(MenuModel).filter_by(id=str(menu.id.value)).first()
        if menu_model:
            menu_model.update_from_domain(menu)

    def find_by_restaurant_id(self, restaurant_id: RestaurantIdVo) -> Optional[Menu]:
        menu_model = self.session.query(MenuModel).filter_by(restaurant_id=str(restaurant_id.value)).first()
        if menu_model:
            return menu_model.to_domain()
        return None
