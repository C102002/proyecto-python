from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_dish_id_exception import InvalidDishIdException
import uuid

class DishIdVo(ValueObjectRoot["DishIdVo"]):
    def __init__(self, value: str | None = None):
        if value is None:
            self.__value = str(uuid.uuid4())
        else:
            self.__value = value

    def equals(self, value: "DishIdVo") -> bool:
        return self.__value == value.__value