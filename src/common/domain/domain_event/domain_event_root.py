from abc import ABC, abstractmethod
from datetime import datetime

class DomainEventRoot(ABC):
    def __init__(self):
        self._ocurred_on = datetime.now()
        self._event_name = self.__class__.__name__

    @property
    def ocurred_on(self) -> datetime:
        return self._ocurred_on

    @property
    def event_name(self) -> str:
        return self._event_name

    @abstractmethod
    def serialize(self) -> str:
        pass