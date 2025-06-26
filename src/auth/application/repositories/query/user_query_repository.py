from abc import ABC, abstractmethod
from src.common.utils import Result
from src.auth.domain.aggregate.user import User

class IUserQueryRepository(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: str) -> Result[User]:
        pass

    @abstractmethod
    async def get_user_email(self, email: str) -> Result[User]:
        pass

    @abstractmethod
    async def get_all_users(self) -> Result[list[User]]:
        pass