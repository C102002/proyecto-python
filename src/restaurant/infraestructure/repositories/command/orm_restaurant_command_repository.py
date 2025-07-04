from src.common.infrastructure.infrastructure_exception.enum.infraestructure_exception_type import ExceptionInfrastructureType
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from sqlalchemy.ext.asyncio import AsyncSession

from src.restaurant.application.repositories.command.restaurant_command_repository import IRestaurantCommandRepository
from src.restaurant.domain.aggregate.restaurant import Restaurant
from src.restaurant.infraestructure.models.orm_restaurant_model import OrmRestaurantModel

class OrmRestaurantCommandRepository(IRestaurantCommandRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def save(self, restaurant: Restaurant) -> Result[Restaurant]:
        try:
            # Continuar aca
            orm_user = OrmRestaurantModel(
                id=restaurant.id.restaurant_id,
                lat=restaurant.location.lat,
                lng=restaurant.location.lng,
                name=restaurant.name.name,
                opening_time=restaurant.opening_time.opening_time,
                closing_time=restaurant.closing_time.closing_time
            )
            self.session.add(orm_user)
            await self.session.commit()
            return Result.success(restaurant)
        
        except Exception as e:
            await self.session.rollback()
            err = InfrastructureException(str(e))
            return Result.fail(err)

    
    async def delete(self, restaurant: Restaurant) -> Result[Restaurant]:
        try:
            existing = await self.session.get(
                OrmRestaurantModel,
                restaurant.id.restaurant_id
            )
            if not existing:
                return Result.fail(
                    InfrastructureException("Restaurante no encontrado",ExceptionInfrastructureType.NOT_FOUND)
                )

            # 2) Márcalo para borrado
            await self.session.delete(existing)
            await self.session.commit()

            return Result.success(restaurant)

        except Exception as e:
            await self.session.rollback()
            err = InfrastructureException(str(e))
            return Result.fail(err)
