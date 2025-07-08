from src.common.infrastructure import InfrastructureException
from src.common.infrastructure.infrastructure_exception.enum.infraestructure_exception_type import ExceptionInfrastructureType

class ReservationNotFoundException(InfrastructureException):

    def __init__(self, ):
        super().__init__("Reservation not found",infra_type=ExceptionInfrastructureType.NOT_FOUND)