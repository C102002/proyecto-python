from typing import List
from src.common.infrastructure.infrastructure_exception.enum.infraestructure_exception_type import ExceptionInfrastructureType
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from sqlalchemy.ext.asyncio import AsyncSession

from src.restaurant.application.repositories.command.restaurant_command_repository import IRestaurantCommandRepository
from src.restaurant.domain.aggregate.restaurant import Restaurant
from src.restaurant.infraestructure.models.orm_restaurant_model import OrmRestaurantModel
from src.restaurant.infraestructure.models.orm_table_model import OrmTableModel

class OrmRestaurantCommandRepository(IRestaurantCommandRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def save(self, restaurant: Restaurant) -> Result[Restaurant]:
        try:
            orm_tables:List[OrmTableModel] = []
            for tbl in restaurant.tables:
                orm_tables.append(
                    OrmTableModel(
                        id=tbl.id.table_number_id,
                        capacity=tbl.capacity.capacity,
                        location=tbl.location.location.value,
                        restaurant_id=restaurant.id.restaurant_id
                    )
                )
            print(f"orm_tables:{orm_tables}")
            # Continuar aca
            orm_restaurant = OrmRestaurantModel(
                id=restaurant.id.restaurant_id,
                lat=restaurant.location.lat,
                lng=restaurant.location.lng,
                name=restaurant.name.name,
                opening_time=restaurant.opening_time.opening_time,
                closing_time=restaurant.closing_time.closing_time
            )
            
            self.session.add(orm_restaurant)
            self.session.add_all(orm_tables)
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
