from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_dish_name_exception import InvalidDishNameException

class DishNameVo(ValueObjectRoot[str]):
    def __init__(self, value: str):
        super().__init__(value)
        if len(value) < 3 or len(value) > 50:
            raise InvalidDishNameException(value)
