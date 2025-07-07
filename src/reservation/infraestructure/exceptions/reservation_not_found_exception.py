from src.common.infrastructure import InfrastructureException

class ReservationNotFoundException(InfrastructureException):

    def __init__(self, ):
        super().__init__("Reservation not found")