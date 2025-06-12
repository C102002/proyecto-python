from src.common.domain import DomainException

class InvalidUserNameException(DomainException):

    def __init__(self, name: str):
        super().__init__(f"Invalid user name: {name}")