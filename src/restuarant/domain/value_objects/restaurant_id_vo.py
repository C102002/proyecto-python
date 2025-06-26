from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_restaurant_id_exception import InvalidRestaurantIdException
import uuid

class RestaurantIdVo(ValueObjectRoot["RestaurantIdVo"]):
    def __init__(self, user_id: str):
        try:
            uuid.UUID(user_id)
        except ValueError:
            raise InvalidRestaurantIdException(user_id)
        
        self.__user_id = user_id

    def equals(self, value: "RestaurantIdVo") -> bool:
        return self.__user_id == value.user_id
    
    @property
    def user_id(self) -> str:
        return self.__user_id