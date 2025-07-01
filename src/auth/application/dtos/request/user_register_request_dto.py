from src.auth.domain.enum.user_role_enum import UserRoleEnum

class UserRegisterRequestDto:

    def __init__(self, email: str, name: str, password: str, role: UserRoleEnum):
        self.email = email
        self.name = name
        self.password = password
        self.role = role