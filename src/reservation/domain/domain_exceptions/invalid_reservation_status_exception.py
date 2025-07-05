from src.common.domain import DomainException

class InvalidReservationStatusException(DomainException):

    def __init__(self, status: str):
        super().__init__("Invalid Reservation Status", status)