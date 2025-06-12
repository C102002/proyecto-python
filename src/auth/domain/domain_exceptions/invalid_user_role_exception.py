from src.common.domain import DomainException

class InvalidUserRoleException(DomainException):

    def __init__(self, role: str):
        super().__init__(f"Invalid user role: {role}")