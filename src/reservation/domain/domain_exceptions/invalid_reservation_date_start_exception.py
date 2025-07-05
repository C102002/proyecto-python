from datetime import time
from src.common.domain import DomainException

class InvalidReservationDateStartException(DomainException):
    
    def __init__(self, entry: time):
        super().__init__(f"Invalid Reservation Date Start: {entry}")