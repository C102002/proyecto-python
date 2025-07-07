from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_dish_name_exception import InvalidDishNameException

class DishNameVo(ValueObjectRoot["DishNameVo"]):
    def __init__(self, value: str):
        if len(value) < 3 or len(value) > 50:
            raise InvalidDishNameException(value)
        
        self.__value = value

    def equals(self, value: "DishNameVo") -> bool:
        return self.__value == value.__value

    @property
    def value(self) -> str:
        return self.__value