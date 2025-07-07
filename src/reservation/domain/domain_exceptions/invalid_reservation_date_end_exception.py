from datetime import time
from src.common.domain import DomainException

class InvalidReservationDateEndException(DomainException):
    
    def __init__(self, entry: time):
        super().__init__(f"Invalid Reservation DateEnd: {entry}")