from src.common.domain import DomainException

class InvalidDishIdException(DomainException):
    def __init__(self, dish_id: str):
        super().__init__(f"Invalid dish id: {dish_id}")
