from src.common.utils.base_exception import BaseException

class InvalidDishIdException(BaseException):
    def __init__(self, dish_id: str):
        super().__init__(f"Invalid dish id: {dish_id}")
