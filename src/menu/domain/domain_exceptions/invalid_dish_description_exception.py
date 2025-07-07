from src.common.utils.base_exception import BaseException

class InvalidDishDescriptionException(BaseException):
    def __init__(self, description: str):
        super().__init__(f"Invalid dish description: {description}, must be less than 255 characters long.")
