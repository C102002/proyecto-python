from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, literal_column
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository
from src.reservation.domain.aggregate.reservation import Reservation
from src.reservation.infraestructure.exceptions.reservation_not_found_exception import ReservationNotFoundException

class OrmReservationQueryRepository(IReservationQueryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_by_id(self, id: str) -> Result[Reservation]:
        pass

    async def get_active_by_client_id(self, client_id: str) -> Result[list[Reservation]]:
        pass

    async def get_all_by_date_restaurant(self) -> Result[list[Reservation]]:
        pass

    async def get_all(self) -> Result[list[Reservation]]:
        pass
    
    """
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
                return Result.fail(ReservationNotFoundException())

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
                return Result.fail(ReservationNotFoundException())

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
    """