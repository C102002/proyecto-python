from src.auth.application.repositories.command.user_command_repository import IUserCommandRepository
from src.auth.domain.aggregate.user import User
from src.common.utils import Result
from src.auth.infrastructure.exceptions.user_not_found_exception import UserNotFoundException

class UserCommandRepositoryMock(IUserCommandRepository):
    
    def __init__(self, shared_user_list: list[User]) -> None:
        self.user_store = shared_user_list

    async def save(self, user: User) -> Result[User]:
        self.user_store.append(user)
        return Result.success(user)
    
    async def update(self, user: User) -> Result[User]:
        for i, u in enumerate(self.user_store):
            if u.id == user.id:
                self.user_store[i] = user
                return Result.success(user)
        return Result.fail(UserNotFoundException())
