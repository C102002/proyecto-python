from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_user_password_exception import InvalidUserPasswordException

class UserPasswordVo(ValueObjectRoot["UserPasswordVo"]):
    def __init__(self, password: str):
        if not password or len(password) < 8:
            raise InvalidUserPasswordException(password)
        
        self.__password = password

    def equals(self, value: "UserPasswordVo") -> bool:
        return self.__password == value.password
    
    @property
    def password(self) -> str:
        return self.__password