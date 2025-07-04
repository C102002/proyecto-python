from src.common.utils.base_exception import BaseException

class DishAlreadyExistsException(BaseException):
    def __init__(self, dish_name: str):
        super().__init__(f"Dish with name '{dish_name}' already exists in the menu.")
