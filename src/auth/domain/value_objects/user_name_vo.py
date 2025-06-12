from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_user_name_exception import InvalidUserNameException

class UserNameVo(ValueObjectRoot["UserNameVo"]):
    def __init__(self, name: str):
        if not name or len(name) < 3:
            raise InvalidUserNameException(name)
        
        self.__name = name

    def equals(self, value: "UserNameVo") -> bool:
        return self.__name == value.name
    
    @property
    def name(self) -> str:
        return self.__name