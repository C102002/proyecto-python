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
from src.restaurant.application.dtos.request.get_all_restaurant_request_dto import GetAllRestaurantRequestDTO
from src.restaurant.application.repositories.query.restaurant_query_repository import IRestaurantQueryRepository
from src.restaurant.domain.aggregate.restaurant import Restaurant
from src.restaurant.domain.value_objects.restaurant_closing_time_vo import RestaurantClosingTimeVo
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo
from src.restaurant.domain.value_objects.restaurant_location_vo import RestaurantLocationVo
from src.restaurant.domain.value_objects.restaurant_name_vo import RestaurantNameVo
from src.restaurant.domain.value_objects.restaurant_opening_time_vo import RestaurantOpeningTimeVo
from src.restaurant.infraestructure.models.orm_restaurant_model import OrmRestaurantModel

class OrmRestaurantQueryRepository(IRestaurantQueryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_by_id(self, restaurant_id: str) -> Result[Restaurant]:
        pass

    async def get_all_restaurants(
        self,
        dto: GetAllRestaurantRequestDTO
    ) -> Result[list[Restaurant]]:

        try:
            # Construye la query con paginación
            stmt = (
                select(OrmRestaurantModel)
                .offset(dto.offset)   # salta (page-1)*size filas
                .limit(dto.limit)     # trae como máximo size filas
            )

            result = await self.session.execute(stmt)
            orm_restaurants = result.scalars().all()

            restaurants: list[Restaurant] = []
            for orm in orm_restaurants:
                restaurant = Restaurant(
                    id=RestaurantIdVo(orm.id),
                    name=RestaurantNameVo(orm.name),
                    location=RestaurantLocationVo(orm.lat, orm.lng),
                    opening_time=RestaurantOpeningTimeVo(orm.opening_time),
                    closing_time=RestaurantClosingTimeVo(orm.closing_time),
                )
                restaurants.append(restaurant)

            return Result.success(restaurants)

        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))
        

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
        
    async def exists_user_by_email(self, email: str) -> Result[bool]:
        try:
            result = await self.session.execute(
                select(OrmUserModel).where(literal_column("email") == email)
            )
            orm_user = result.scalars().first()

            return Result.success(orm_user is not None)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))