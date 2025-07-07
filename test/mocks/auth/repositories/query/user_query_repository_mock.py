from src.auth.application.repositories.query.user_query_repository import IUserQueryRepository
from src.auth.domain.aggregate.user import User
from src.common.utils import Result
from src.auth.infrastructure.exceptions.user_not_found_exception import UserNotFoundException

class UserQueryRepositoryMock(IUserQueryRepository):

    def __init__(self, shared_user_list: list[User]) -> None:
        self.user_store = shared_user_list

    async def get_all_users(self) -> Result[list[User]]:
        return Result.success(self.user_store)
    
    async def get_user_email(self, email: str) -> Result[User]:
        user = next((u for u in self.user_store if u.email.email == email), None)
        if user:
            return Result.success(user)
        return Result.fail(UserNotFoundException())
    
    async def get_by_id(self, user_id: str) -> Result[User]:
        user = next((u for u in self.user_store if u.id.user_id == user_id), None)
        if user:
            return Result.success(user)
        return Result.fail(UserNotFoundException())
    
    async def exists_user_by_email(self, email: str) -> Result[bool]:
        user = next((u for u in self.user_store if u.email.email == email), None)
        return Result.success(user is not None)
