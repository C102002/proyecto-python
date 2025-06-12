from src.common.domain import DomainException

class InvalidUserPasswordException(DomainException):

    def __init__(self, password: str):
        super().__init__(f"Invalid user password: {password}")