from src.common.utils import BaseException
from src.common.utils import BaseExceptionEnum

class InfrastructureException(BaseException):

    def __init__(self, message: str):
        super().__init__(message, BaseExceptionEnum.INFRASTRUCTURE_EXCEPTION)