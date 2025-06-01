from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from src.common.utils import Result

I = TypeVar('I')
O = TypeVar('O')

class IService(ABC, Generic[I, O]):
    @abstractmethod
    async def execute(self, value: I) -> Result[O]:
        pass

    @property
    def class_name(self) -> str:
        return self.__class__.__name__