from src.common.domain import DomainException

class InvalidUserException(DomainException):

    def __init__(self):
        super().__init__("Invalid user")