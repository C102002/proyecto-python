from typing import Generic, TypeVar
from src.common.utils import Result
from ...decorators.base_service_decorator import BaseServiceDecorator
from ...service.service import IService

I = TypeVar('I')
O = TypeVar('O')

class ExceptionDecorator(BaseServiceDecorator[I, O], Generic[I, O]):
    def __init__(self, service: IService[I, O]):
        super().__init__(service)

    async def execute(self, value: I) -> Result[O]:
        try:
            response = await self.service.execute(value)
            if response.is_error:
                raise response.error
            return response
        except Exception as err:
            raise err