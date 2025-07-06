from src.common.utils import BaseException
from src.common.utils import BaseExceptionEnum
from .enum.application_exception_type import ExceptionApplicationType

class ApplicationException(BaseException):
    def __init__(self, message: str, app_type: ExceptionApplicationType = ExceptionApplicationType.APPLICATION_ERROR):
        self._app_type = app_type
        super().__init__(message, BaseExceptionEnum.APPLICATION_EXCEPTION)
    
    def get_application_type(self) -> ExceptionApplicationType:
        return self._app_type