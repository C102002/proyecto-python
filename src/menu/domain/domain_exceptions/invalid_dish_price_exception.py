from src.common.utils.base_exception import BaseException

class InvalidDishPriceException(BaseException):
    def __init__(self, price: float):
        super().__init__(f"Invalid dish price: {price}, must be greater than 0.")
