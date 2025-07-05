from src.common.domain import DomainException

class InvalidTableUpdateException(DomainException):

    def __init__(self, number: int):
        super().__init__(f"Invalid table update: the table number {number} is not in the restaurant tables ")