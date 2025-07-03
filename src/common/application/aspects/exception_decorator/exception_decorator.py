from typing import Generic, TypeVar

from src.common.utils.base_exception import BaseException
from src.common.application.error_handler.error_handler import IErrorHandler
from src.common.domain.domain_exception.domain_exception import DomainException
from src.common.utils import Result
from ...decorators.base_service_decorator import BaseServiceDecorator
from ...service.service import IService

I = TypeVar('I')
O = TypeVar('O')

class ExceptionDecorator(BaseServiceDecorator[I, O], Generic[I, O]):
    def __init__(self, service: IService[I, O], error_handler:IErrorHandler):
        super().__init__(service)
        self.error_handler=error_handler

    async def execute(self, value: I) -> Result[O]:
        try:
            response = await self.service.execute(value)
            if response.is_error:
                raise self.error_handler.to_http(response.error,str(response.error))
            return response

        # 2. Si es una de tus excepciones de negocio, lo mapeas a HTTP
        except BaseException as err:
            if isinstance(err,DomainException):
                raise self.error_handler.to_http(err, str(err))
