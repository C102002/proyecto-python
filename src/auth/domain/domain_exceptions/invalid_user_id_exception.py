from src.common.domain import DomainException

class InvalidUserIdException(DomainException):
    
    def __init__(self, user_id: str):
        super().__init__(f"Invalid user ID: {user_id}")