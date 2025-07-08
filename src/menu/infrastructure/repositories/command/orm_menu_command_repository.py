from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, literal_column
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
        print("debug")

    async def update(self, menu: Menu) -> None:
        menu_model = await self.session.execute(
                select(MenuModel).where(literal_column("id") == menu.id.value)
            )
        result = menu_model.scalars().first()
        print("haciendo debug", result)
        if result:
            result.update_from_domain(menu)
            self.session.add(result)
            await self.session.commit()

