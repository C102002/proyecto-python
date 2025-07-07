from src.common.domain.value_object.value_object_root import ValueObjectRoot

class DishImageVo(ValueObjectRoot["DishImageVo"]):
    def __init__(self, value: str | None = None):
        self.__value = value
    
    def equals(self, value: "DishImageVo") -> bool:
        return self.__value == value.__value
    
    @property
    def value(self) -> str | None:
        return self.__value
