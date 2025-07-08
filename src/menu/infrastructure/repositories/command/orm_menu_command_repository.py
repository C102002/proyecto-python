from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from src.menu.application.repositories.command.menu_command_repository import MenuCommandRepository
from src.menu.domain.aggregate.menu import Menu
from src.menu.infrastructure.models.menu_model import MenuModel

class OrmMenuCommandRepository(MenuCommandRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, menu: Menu) -> None:
        menu_model = MenuModel.from_domain(menu)
        self.session.add(menu_model)
        await self.session.commit()

    async def update(self, menu: Menu) -> None:
        menu_model = await self.session.execute(
                select(MenuModel).where(MenuModel.id == menu.id.value).options(joinedload(MenuModel.dishes))
            )
        result = menu_model.scalars().first()
        if result:
            result.update_from_domain(menu)
            self.session.add(result)
            await self.session.commit()

