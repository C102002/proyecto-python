from src.common.utils.base_exception import BaseException

class DishNotFoundException(BaseException):
    def __init__(self, dish_id: str):
        super().__init__(f"Dish with id '{dish_id}' not found in the menu.")
