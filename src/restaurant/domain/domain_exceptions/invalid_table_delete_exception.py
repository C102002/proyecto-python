from src.common.domain import DomainException

class InvalidTableDeleteException(DomainException):

    def __init__(self, number: int):
        super().__init__(f"Invalid table delete: the table number {number} is not in the restaurant tables ")