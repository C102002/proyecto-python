from src.menu.application.repositories.command.menu_command_repository import MenuCommandRepository
from src.menu.domain.aggregate.menu import Menu

class MenuCommandRepositoryMock(MenuCommandRepository):

    def __init__(self, menu_store: list[Menu]) -> None:
        self.menu_store = menu_store

    async def save(self, menu: Menu) -> None:
        self.menu_store.append(menu)
    
    async def update(self, menu: Menu) -> None:
        for i, u in enumerate(self.menu_store):
            if u.id.value == menu.id.value:
                self.menu_store[i] = menu