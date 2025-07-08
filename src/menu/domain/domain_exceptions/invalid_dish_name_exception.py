from src.common.domain import DomainException

class InvalidDishNameException(DomainException):
    def __init__(self, name: str):
        super().__init__(f"Invalid dish name: {name}, must be between 3 and 50 characters long.")
