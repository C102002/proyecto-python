from datetime import date
from src.common.domain import DomainException

class InvalidReservationDateException(DomainException):
    
    def __init__(self, entry: date):
        super().__init__(f"Invalid Reservation Date: {entry}")