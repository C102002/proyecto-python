from abc import ABC, abstractmethod
from typing import List
from src.auth.domain.aggregate.user import User
from src.common.utils import Result

class IUserCommandRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> Result[User]:
        pass

    @abstractmethod
    async def update(self, user: User) -> Result[User]:
        pass