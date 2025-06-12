from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_user_email_exception import InvalidUserEmailException
import re

class UserEmailVo(ValueObjectRoot["UserEmailVo"]):
    
    def __init__(self, email: str):
        regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(regex_email, email):
            raise InvalidUserEmailException(email)
        
        self.__email = email

    def equals(self, value: "UserEmailVo") -> bool:
        return self.__email == value.email
    
    @property
    def email(self) -> str:
        return self.__email
