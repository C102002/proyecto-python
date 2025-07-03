from src.common.domain import DomainException

class InvalidTableCapacity(DomainException):
    
    def __init__(self, capacity: int):
        super().__init__(f"Invalid Capacity of table: {capacity}, table must be greater or equeals than 2 and lower and equals than 12 ")