from abc import ABC, abstractmethod
from src.auth.domain.enum.user_role_enum import UserRoleEnum

class ITokenGenerator(ABC):

    @abstractmethod
    def generate_token(self, data: dict, role: UserRoleEnum) -> str:
        pass

    @abstractmethod
    def decode_token(self, token: str) -> dict:
        pass