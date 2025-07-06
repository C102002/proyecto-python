from src.common.infrastructure.infrastructure_exception.enum.infraestructure_exception_type import ExceptionInfrastructureType
from src.common.utils import BaseException
from src.common.utils import BaseExceptionEnum

class InfrastructureException(BaseException):

    def __init__(self, message: str, infra_type: ExceptionInfrastructureType = ExceptionInfrastructureType.INTERNAL_SERVER_ERROR):
        self._infra_type = infra_type
        super().__init__(message, BaseExceptionEnum.INFRASTRUCTURE_EXCEPTION)
        
    def get_infrastructure_type(self) -> ExceptionInfrastructureType:
        """
        Devuelve el tipo de excepción de infraestructura.
        """
        return self._infra_type