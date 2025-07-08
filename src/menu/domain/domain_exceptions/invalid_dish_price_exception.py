from src.common.domain import DomainException

class InvalidDishPriceException(DomainException):
    def __init__(self, price: float):
        super().__init__(f"Invalid dish price: {price}, must be greater than 0.")
