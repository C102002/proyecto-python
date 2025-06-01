from src.common.utils import BaseException
from src.common.utils import BaseExceptionEnum

class ApplicationException(BaseException):
    def __init__(self, message: str):
        super().__init__(message, BaseExceptionEnum.APPLICATION_EXCEPTION)