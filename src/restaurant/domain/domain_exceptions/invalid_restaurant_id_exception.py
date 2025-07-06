from src.common.domain import DomainException

class InvalidRestaurantIdException(DomainException):
    
    def __init__(self, user_id: str):
        super().__init__(f"Invalid Restaurant ID: {user_id}")