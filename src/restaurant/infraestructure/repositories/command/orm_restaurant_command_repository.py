from typing import List

from sqlalchemy import delete, insert, select
from src.common.infrastructure.infrastructure_exception.enum.infraestructure_exception_type import ExceptionInfrastructureType
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from sqlalchemy.ext.asyncio import AsyncSession

from src.restaurant.application.dtos.request.delete_table_by_id_request_dto import DeleteTableByIdRequestDTO
from src.restaurant.application.repositories.command.restaurant_command_repository import IRestaurantCommandRepository
from src.restaurant.domain.aggregate.restaurant import Restaurant
from src.restaurant.domain.entities.table import Table
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
        
    async def delete_table(
        self,
        data: DeleteTableByIdRequestDTO
    ) -> Result[DeleteTableByIdRequestDTO]:
        try:
            stmt = delete(OrmTableModel).where(
                OrmTableModel.restaurant_id == data.restaurant_id,
                OrmTableModel.id        == data.table_id
            )
            result = await self.session.execute(stmt)

            # Opcional: si esperas saber si realmente borró algo
            if result.rowcount == 0:
                return Result.fail(
                    InfrastructureException(
                        "Table not found",
                        ExceptionInfrastructureType.NOT_FOUND
                    )
                )

            await self.session.commit()
            return Result.success(data)

        except Exception as e:
            await self.session.rollback()
            return Result.fail(InfrastructureException(str(e),ExceptionInfrastructureType.BAD_REQUEST))
        
    async def add_table(
        self, 
        restaurant: Restaurant, 
        table: Table
    ) -> Result[Restaurant]:
        try:
            orm_data = OrmTableModel(
                id=table.id.table_number_id,
                capacity=table.capacity.capacity,
                location=table.location.location,
                restaurant_id=restaurant.id.restaurant_id
            )

            # 3) INSERT en BD
            self.session.add(orm_data)
            await self.session.commit()

            # 4) Devolver el agregado con éxito
            return Result.success(restaurant)

        except Exception as e:
            # Cualquier otro error de infraestructura
            await self.session.rollback()
            return Result.fail(
                InfrastructureException(
                    str(e),
                    ExceptionInfrastructureType.BAD_REQUEST
                )
            )
            
    async def update_restaurant(self, restaurant: Restaurant) -> Result[Restaurant]:
        try:
            
            stmt = select(OrmRestaurantModel).where(
                OrmRestaurantModel.id == restaurant.id.restaurant_id
            )
            result = await self.session.execute(stmt)
            orm_rest = result.scalar_one_or_none()

            if orm_rest is None:
                return Result.fail(
                    InfrastructureException(
                        "Restaurant not found",
                        ExceptionInfrastructureType.NOT_FOUND
                    )
                )

            orm_rest.name         = restaurant.name.name
            orm_rest.lat          = restaurant.location.lat
            orm_rest.lng          = restaurant.location.lng
            orm_rest.opening_time = restaurant.opening_time.opening_time
            orm_rest.closing_time = restaurant.closing_time.closing_time

            self.session.add(orm_rest)
            await self.session.commit()

            return Result.success(restaurant)

        except Exception as e:
            await self.session.rollback()
            return Result.fail(
                InfrastructureException(
                    str(e),
                    ExceptionInfrastructureType.BAD_REQUEST
                )
            )
