from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, literal_column
from src.common.infrastructure.infrastructure_exception.enum.infraestructure_exception_type import ExceptionInfrastructureType
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from src.restaurant.application.dtos.request.get_all_restaurant_request_dto import GetAllRestaurantRequestDTO
from src.restaurant.application.repositories.query.restaurant_query_repository import IRestaurantQueryRepository
from src.restaurant.domain.aggregate.restaurant import Restaurant
from src.restaurant.domain.entities.table import Table
from src.restaurant.domain.entities.value_objects.table_capacity_vo import TableCapacityVo
from src.restaurant.domain.entities.value_objects.table_location_vo import TableLocationVo
from src.restaurant.domain.entities.value_objects.table_number_id_vo import TableNumberId
from src.restaurant.domain.value_objects.restaurant_closing_time_vo import RestaurantClosingTimeVo
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo
from src.restaurant.domain.value_objects.restaurant_location_vo import RestaurantLocationVo
from src.restaurant.domain.value_objects.restaurant_name_vo import RestaurantNameVo
from src.restaurant.domain.value_objects.restaurant_opening_time_vo import RestaurantOpeningTimeVo
from src.restaurant.infraestructure.models.orm_restaurant_model import OrmRestaurantModel
from src.restaurant.infraestructure.models.orm_table_model import OrmTableModel

class OrmRestaurantQueryRepository(IRestaurantQueryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_by_id(self, restaurant_id: str) -> Result[Restaurant]:
        try:
            result = await self.session.execute(
                select(OrmRestaurantModel).where(literal_column("id") == restaurant_id)
            )
            orm_restaurant = result.scalars().first()
            
            if orm_restaurant is None:
                return Result.fail(InfrastructureException("Restaurant not found",ExceptionInfrastructureType.NOT_FOUND))
            
            # 2) Traer las mesas asociadas
            q = (
                select(OrmTableModel)
                .where(OrmTableModel.restaurant_id == orm_restaurant.id)
                .order_by(OrmTableModel.capacity)
            )
            tbl_res = await self.session.execute(q)
            orm_tables = tbl_res.scalars().all()
                        

            restaurant = Restaurant(
                id=RestaurantIdVo(orm_restaurant.id),
                name=RestaurantNameVo(orm_restaurant.name),
                location=RestaurantLocationVo(orm_restaurant.lat, orm_restaurant.lng),
                opening_time=RestaurantOpeningTimeVo(orm_restaurant.opening_time),
                closing_time=RestaurantClosingTimeVo(orm_restaurant.closing_time),
                tables=[
                    Table(
                        id=TableNumberId(orm_table.id),
                        location=TableLocationVo(orm_table.location.value),
                        capacity=TableCapacityVo(orm_table.capacity)
                    )
                    for orm_table in orm_tables
                ]
            )
                        
            return Result.success(restaurant)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))
        
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
            for orm_restaurant in orm_restaurants:
                restaurant = Restaurant(
                    id=RestaurantIdVo(orm_restaurant.id),
                    name=RestaurantNameVo(orm_restaurant.name),
                    location=RestaurantLocationVo(orm_restaurant.lat, orm_restaurant.lng),
                    opening_time=RestaurantOpeningTimeVo(orm_restaurant.opening_time),
                    closing_time=RestaurantClosingTimeVo(orm_restaurant.closing_time),
                )
                restaurants.append(restaurant)

            return Result.success(restaurants)

        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))