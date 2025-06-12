from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_user_role_exception import InvalidUserRoleException
from ..enum.user_role_enum import UserRoleEnum

class UserRoleVo(ValueObjectRoot["UserRoleVo"]):
    
    def __init__(self, role: str):

        if not isinstance(role, UserRoleEnum):
            raise InvalidUserRoleException(role)
        
        self.__role = role

    def equals(self, value: "UserRoleVo") -> bool:
        return self.__role == value.role
    
    @property
    def role(self) -> UserRoleEnum:
        return self.__role