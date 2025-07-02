from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_restaurant_name_exception import InvalidRestaurantNameException

class RestaurantNameVo(ValueObjectRoot["RestaurantNameVo"]):
    def __init__(self, name: str):
        if not name or len(name) < 3:
            raise InvalidRestaurantNameException(name)
        
        self.__name = name

    def equals(self, value: "RestaurantNameVo") -> bool:
        return self.__name == value.name
    
    @property
    def name(self) -> str:
        return self.__name