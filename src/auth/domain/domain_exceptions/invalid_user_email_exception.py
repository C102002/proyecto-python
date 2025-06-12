from src.common.domain import DomainException

class InvalidUserEmailException(DomainException):

    def __init__(self, email: str):
        super().__init__(f"Invalid user email: {email}")