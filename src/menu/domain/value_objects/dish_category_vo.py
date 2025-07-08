from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_dish_category_exception import InvalidDishCategoryException

class DishCategoryVo(ValueObjectRoot["DishCategoryVo"]):
    SUPPORTED_CATEGORIES = ["Main", "Dessert", "Appetizer"]

    def __init__(self, value: str):
        if value not in self.SUPPORTED_CATEGORIES:
            raise InvalidDishCategoryException(value)
        
        self.__value = value

    def equals(self, value: "DishCategoryVo") -> bool:
        return self.__value == value.__value

    @property
    def value(self) -> str:
        return self.__value
