from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from src.common.utils import Result
from ..service.service import IService

I = TypeVar('I')
O = TypeVar('O')

class BaseServiceDecorator(IService[I, O], ABC, Generic[I, O]):
    def __init__(self, service: IService[I, O]):
        self.service = service
        super().__init__()

    @abstractmethod
    async def execute(self, value: I) -> Result[O]:
        pass