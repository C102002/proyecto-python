from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_dish_category_exception import InvalidDishCategoryException

class DishCategoryVo(ValueObjectRoot[str]):
    SUPPORTED_CATEGORIES = ["Main", "Dessert", "Appetizer"]

    def __init__(self, value: str):
        super().__init__(value)
        if value not in self.SUPPORTED_CATEGORIES:
            raise InvalidDishCategoryException(value)
