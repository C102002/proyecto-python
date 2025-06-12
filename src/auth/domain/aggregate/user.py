from src.common.domain import AggregateRoot
from src.common.domain.domain_event.domain_event_root import DomainEventRoot
from ..value_objects.user_id_vo import UserIdVo
from ..value_objects.user_name_vo import UserNameVo
from ..value_objects.user_password_vo import UserPasswordVo
from ..value_objects.user_email_vo import UserEmailVo
from ..value_objects.user_role_vo import UserRoleVo
from ..domain_exceptions.invalid_user_exception import InvalidUserException

class User(AggregateRoot["UserIdVo"]):
    
    def __init__(self, id: UserIdVo, email: UserEmailVo, name: UserNameVo, password: UserPasswordVo, role: UserRoleVo):
        super().__init__(id)
        self.__email = email
        self.__name = name
        self.__password = password
        self.__role = role

    def when(self, event: DomainEventRoot) -> None:
        pass

    def validate_state(self) -> None:
        if not self._id or not self.__email or not self.__name or not self.__password or not self.__role:
            raise InvalidUserException()
        
    def update_email(self, email: UserEmailVo) -> None:
        self.__email = email

    def update_name(self, name: UserNameVo) -> None:
        self.__name = name

    def update_password(self, password: UserPasswordVo) -> None:
        self.__password = password

    @property
    def email(self) -> UserEmailVo:
        return self.__email
    
    @property
    def name(self) -> UserNameVo:
        return self.__name
    
    @property
    def password(self) -> UserPasswordVo:
        return self.__password
    
    @property
    def role(self) -> UserRoleVo:
        return self.__role