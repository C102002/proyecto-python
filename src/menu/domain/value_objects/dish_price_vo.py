from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_dish_price_exception import InvalidDishPriceException

class DishPriceVo(ValueObjectRoot[float]):
    def __init__(self, value: float):
        super().__init__(value)
        if value <= 0:
            raise InvalidDishPriceException(value)
