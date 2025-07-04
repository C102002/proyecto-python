from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_dish_description_exception import InvalidDishDescriptionException

class DishDescriptionVo(ValueObjectRoot[str]):
    def __init__(self, value: str):
        super().__init__(value)
        if len(value) > 255:
            raise InvalidDishDescriptionException(value)
