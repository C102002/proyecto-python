from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_dish_price_exception import InvalidDishPriceException

class DishPriceVo(ValueObjectRoot["DishPriceVo"]):
    def __init__(self, value: float):
        if value <= 0:
            raise InvalidDishPriceException(value)
        
        self.__value = value

    def equals(self, value: "DishPriceVo") -> bool:
        return self.__value == value.__value
    
    @property
    def value(self) -> float:
        return self.__value
