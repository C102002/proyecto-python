from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_dish_description_exception import InvalidDishDescriptionException

class DishDescriptionVo(ValueObjectRoot["DishDescriptionVo"]):
    def __init__(self, value: str):
        if len(value) > 255:
            raise InvalidDishDescriptionException(value)
        
        self.__value = value

    def equals(self, value: "DishDescriptionVo") -> bool:
        return self.__value == value.__value
    
    @property
    def value(self) -> str:
        return self.__value
