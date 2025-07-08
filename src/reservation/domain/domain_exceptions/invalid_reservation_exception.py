from src.common.domain import DomainException

class InvalidReservationException(DomainException):

    def __init__(self):
        super().__init__("Invalid Reservation")