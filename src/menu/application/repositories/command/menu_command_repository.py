from abc import ABC, abstractmethod
from src.menu.domain.aggregate.menu import Menu

class MenuCommandRepository(ABC):

    @abstractmethod
    async def save(self, menu: Menu) -> None:
        pass

    @abstractmethod
    async def update(self, menu: Menu) -> None:
        pass
