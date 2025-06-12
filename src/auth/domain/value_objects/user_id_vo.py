from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_user_id_exception import InvalidUserIdException
import uuid

class UserIdVo(ValueObjectRoot["UserIdVo"]):
    def __init__(self, user_id: str):
        try:
            uuid.UUID(user_id)
        except ValueError:
            raise InvalidUserIdException(user_id)
        
        self.__user_id = user_id

    def equals(self, value: "UserIdVo") -> bool:
        return self.__user_id == value.user_id
    
    @property
    def user_id(self) -> str:
        return self.__user_id