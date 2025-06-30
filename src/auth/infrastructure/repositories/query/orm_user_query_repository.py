from src.auth.application.repositories.query.user_query_repository import IUserQueryRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.infrastructure.models.orm_user_model import OrmUserModel
from sqlalchemy import select, literal_column
from src.auth.domain.aggregate.user import User
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from src.auth.domain.value_objects.user_email_vo import UserEmailVo
from src.auth.domain.value_objects.user_id_vo import UserIdVo
from src.auth.domain.value_objects.user_name_vo import UserNameVo
from src.auth.domain.value_objects.user_password_vo import UserPasswordVo
from src.auth.domain.value_objects.user_role_vo import UserRoleVo

class OrmUserQueryRepository(IUserQueryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_users(self) -> Result[list[User]]:
        try:
            result = await self.session.execute(select(OrmUserModel))
            orm_users = result.scalars().all()
            
            users: list[User] = []

            for orm_user in orm_users:
                user = User(
                    id=UserIdVo(orm_user.id),
                    email=UserEmailVo(orm_user.email),
                    name=UserNameVo(orm_user.name),
                    password=UserPasswordVo(orm_user.password),
                    role=UserRoleVo(orm_user.role)
                )
                users.append(user)

            return Result.success(users)

        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))
        
    async def get_by_id(self, user_id: str) -> Result[User]:
        try:
            result = await self.session.execute(
                select(OrmUserModel).where(literal_column("id") == user_id)
            )
            orm_user = result.scalars().first()
            if orm_user is None:
                return Result.fail(InfrastructureException("User not found"))

            user = User(
                id=UserIdVo(orm_user.id),
                email=UserEmailVo(orm_user.email),
                name=UserNameVo(orm_user.name),
                password=UserPasswordVo(orm_user.password),
                role=UserRoleVo(orm_user.role)
            )
            return Result.success(user)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))
        
    async def get_user_email(self, email: str) -> Result[User]:
        try:
            result = await self.session.execute(
                select(OrmUserModel).where(literal_column("email") == email)
            )
            orm_user = result.scalars().first()

            if orm_user is None:
                return Result.fail(InfrastructureException("User not found"))

            user = User(
                id=UserIdVo(orm_user.id),
                email=UserEmailVo(orm_user.email),
                name=UserNameVo(orm_user.name),
                password=UserPasswordVo(orm_user.password),
                role=UserRoleVo(orm_user.role)
            )
            return Result.success(user)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))