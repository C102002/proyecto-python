from src.common.domain import DomainException

class InvalidReservationIdException(DomainException):
    
    def __init__(self, user_id: str):
        super().__init__(f"Invalid Reservation ID: {user_id}")