from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, literal_column
from src.menu.application.repositories.query.menu_query_repository import MenuQueryRepository
from src.menu.domain.aggregate.menu import Menu
from src.menu.domain.value_objects.dish_id_vo import DishIdVo
from src.menu.infrastructure.models.menu_model import MenuModel, DishModel
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo

class OrmMenuQueryRepository(MenuQueryRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_by_restaurant_id(self, restaurant_id: RestaurantIdVo) -> Optional[Menu]:
        menu_model = await self.session.execute(
                select(MenuModel).where(literal_column("restaurant_id") == restaurant_id.restaurant_id)
            )
        result = menu_model.scalars().first()
        if result:
            return result.to_domain()
        return None

    async def find_by_dish_id(self, dish_id_vo: DishIdVo) -> Optional[Menu]:
        statement = (
            select(MenuModel)
            .join(DishModel, literal_column("id") == literal_column("menu_id"))
            .where(literal_column("id") == dish_id_vo.value)
        )
        
        result = await self.session.execute(statement)
        
        menu_model = result.scalars().first()

        if menu_model:
            return menu_model.to_domain()
        return None