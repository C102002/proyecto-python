from src.common.domain import DomainException

class DishNotFoundException(DomainException):
    def __init__(self, dish_id: str):
        super().__init__(f"Dish with id '{dish_id}' not found in the menu.")
