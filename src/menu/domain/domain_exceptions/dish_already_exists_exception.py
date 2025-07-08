from src.common.domain import DomainException

class DishAlreadyExistsException(DomainException):
    def __init__(self, dish_name: str):
        super().__init__(f"Dish with name '{dish_name}' already exists in the menu.")
