from src.common.domain import DomainException

class InvalidDishDescriptionException(DomainException):
    def __init__(self, description: str):
        super().__init__(f"Invalid dish description: {description}, must be less than 255 characters long.")
