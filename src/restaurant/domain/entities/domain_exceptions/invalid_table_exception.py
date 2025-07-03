from src.common.domain import DomainException

class InvalidTableException(DomainException):

    def __init__(self):
        super().__init__("Invalid Table")