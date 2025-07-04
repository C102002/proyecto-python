from src.common.domain import DomainException

class InvalidReservationDateStartException(DomainException):
    
    def __init__(self, entry: str):
        super().__init__(f"Invalid Reservation Date Start: {entry}")