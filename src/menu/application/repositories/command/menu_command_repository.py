from abc import ABC, abstractmethod
from src.menu.domain.aggregate.menu import Menu

class MenuCommandRepository(ABC):

    @abstractmethod
    def save(self, menu: Menu) -> None:
        pass

    @abstractmethod
    def update(self, menu: Menu) -> None:
        pass
