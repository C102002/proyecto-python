from src.auth.application.repositories.command.user_command_repository import IUserCommandRepository
from src.auth.domain.aggregate.user import User
from src.auth.infrastructure.models.orm_user_model import OrmUserModel
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from ...exceptions.user_not_found_exception import UserNotFoundException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

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
        
    async def update(self, user: User) -> Result[User]:
        try:
            
            stmt = select(OrmUserModel).where(OrmUserModel.id == user.id.user_id)
            result = await self.session.execute(stmt)
            orm_user_to_update = result.scalar_one_or_none()

            if orm_user_to_update is None:
                err = UserNotFoundException()
                return Result.fail(err)

            orm_user_to_update.email = user.email.email
            orm_user_to_update.name = user.name.name
            orm_user_to_update.password = user.password.password
            orm_user_to_update.role = user.role.role
            
            self.session.add(orm_user_to_update)
            
            await self.session.commit()
            
            return Result.success(user)

        except Exception as e:
            await self.session.rollback()
            err = InfrastructureException(str(e))
            return Result.fail(err)