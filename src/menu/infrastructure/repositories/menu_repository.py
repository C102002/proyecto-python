from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, literal_column
from src.menu.application.repositories.command.menu_command_repository import MenuCommandRepository
from src.menu.application.repositories.query.menu_query_repository import MenuQueryRepository
from src.menu.domain.aggregate.menu import Menu
from src.menu.infrastructure.models.menu_model import MenuModel, DishModel
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo

class MenuRepository(MenuCommandRepository, MenuQueryRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, menu: Menu) -> None:
        menu_model = MenuModel.from_domain(menu)
        self.session.add(menu_model)

    async def update(self, menu: Menu) -> None:
        menu_model = await self.session.execute(
                select(MenuModel).where(literal_column("id") == menu.id.value)
            )
        result = menu_model.scalars().first()
        if result:
            result.update_from_domain(menu)

    async def find_by_restaurant_id(self, restaurant_id: RestaurantIdVo) -> Optional[Menu]:
        menu_model = await self.session.execute(
                select(MenuModel).where(literal_column("restaurant_id") == restaurant_id.value)
            )
        result = menu_model.scalars().first()
        if result:
            return result.to_domain()
        return None
