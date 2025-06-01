from ..base_exception import BaseException
from ..base_exception_enum import BaseExceptionEnum

class NotRegisteredException(BaseException):
    def __init__(self, message: str):
        super().__init__(message, BaseExceptionEnum.NOT_REGISTERED)