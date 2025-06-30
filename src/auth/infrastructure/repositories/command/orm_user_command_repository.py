from src.auth.application.repositories.command.user_command_repository import IUserCommandRepository
from src.auth.domain.aggregate.user import User
from src.auth.infrastructure.models.orm_user_model import OrmUserModel
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from sqlalchemy.ext.asyncio import AsyncSession

class OrmUserCommandRepository(IUserCommandRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, user: User) -> Result[User]:
        try:
            orm_user = OrmUserModel(
                id=user.id.user_id,
                email=user.email.email,
                name=user.name.name,
                password=user.password.password,
                role=user.role.role
            )
            
            self.session.add(orm_user)
            await self.session.commit()
            return Result.success(user)
        
        except Exception as e:
            await self.session.rollback()
            err = InfrastructureException(str(e))
            return Result.fail(err)