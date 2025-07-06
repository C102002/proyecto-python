from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_restaurant_id_exception import InvalidRestaurantIdException
import uuid

class RestaurantIdVo(ValueObjectRoot["RestaurantIdVo"]):
    def __init__(self, restaurant_id: str):
        try:
            uuid.UUID(restaurant_id)
        except ValueError:
            raise InvalidRestaurantIdException(restaurant_id)
        
        self.__restaurant_id = restaurant_id

    def equals(self, value: "RestaurantIdVo") -> bool:
        return self.__restaurant_id == value.__restaurant_id
    
    @property
    def restaurant_id(self) -> str:
        return self.__restaurant_id