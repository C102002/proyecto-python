from datetime import date, time
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, select, literal_column
from src.auth.domain.value_objects.user_id_vo import UserIdVo
from src.common.infrastructure.infrastructure_exception.enum.infraestructure_exception_type import ExceptionInfrastructureType
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository
from src.reservation.domain.aggregate.reservation import Reservation
from src.reservation.domain.value_objects.reservation_date_end_vo import ReservationDateEndVo
from src.reservation.domain.value_objects.reservation_date_start_vo import ReservationDateStartVo
from src.reservation.domain.value_objects.reservation_date_vo import ReservationDateVo
from src.reservation.domain.value_objects.reservation_id_vo import ReservationIdVo
from src.reservation.domain.value_objects.reservation_status_vo import ReservationStatusVo
from src.reservation.infraestructure.models.orm_reservation_model import OrmReservationModel
from src.restaurant.domain.entities.value_objects.table_number_id_vo import TableNumberId
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo

class OrmReservationQueryRepository(IReservationQueryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session
        
    def _map_orm_to_domain(self, orm: OrmReservationModel) -> Reservation:
        """
        Convierte la instancia ORM a la entidad de dominio Reservation
        """
        return Reservation(
            client_id         = UserIdVo(orm.client_id),
            id                = ReservationIdVo(orm.id),
            date_start        = ReservationDateStartVo(orm.date_start),
            date_end          = ReservationDateEndVo(orm.date_end),
            reservation_date  = ReservationDateVo(orm.reservation_date),
            status            = ReservationStatusVo(orm.status),
            table_number_id   = TableNumberId(orm.table_number_id),
            restaurant_id     = RestaurantIdVo(orm.restaurant_id),
            dish              = []  # ajusta según tu lógica de agregados
        )
    
    async def exists_by_date_client(self, date_start: time, date_end: time, client_id: str, reservation_date: date) -> Result[bool]:
        try:
            result = await self.session.execute(
                select(OrmReservationModel).where(
                    and_(
                        literal_column("client_id") == client_id,
                        literal_column("date_start") == date_start,
                        literal_column("date_end") == date_end,
                        literal_column("reservation_date") == reservation_date,
                    )
                )
            )
            oorm = result.scalars().first()
            if oorm is None:
               return Result.success(False)
            return Result.success(True)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))

    async def get_by_id(self, id: str) -> Result[Reservation]:
        try:
            result = await self.session.execute(
                select(OrmReservationModel).where(literal_column("id") == id)
            )
            orm = result.scalars().first()
            
            if orm is None:
               return Result.fail(InfrastructureException(message="Reservation Not Found",infra_type=ExceptionInfrastructureType.NOT_FOUND) )
           
            value = self._map_orm_to_domain(orm)
            
            return Result.success(value)
        except Exception as e:
            print(f"fallo aca {e}")
            return Result.fail(InfrastructureException(str(e)))

    async def exists_by_table(self, table_id: str, date_start: time, date_end: time, reservation_date: date, restaurant_id: str) -> Result[bool]:
        try:
            result = await self.session.execute(
                select(OrmReservationModel).where(
                    and_(
                        literal_column("table_number_id") == table_id,
                        literal_column("date_start") == date_start,
                        literal_column("date_end") == date_end,
                        literal_column("reservation_date") == reservation_date,
                        literal_column("restaurant_id") == restaurant_id,
                    )
                )
            )
            oorm = result.scalars().first()
            print(oorm, flush=True)
            if oorm is None:
               return Result.success(False)
            return Result.success(True)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))

    async def get_active_by_client_id(self, client_id: str) -> Result[list[Reservation]]:
        try:
            result = await self.session.execute(
                select(OrmReservationModel).where(
                    and_(
                        literal_column("client_id") == client_id,
                        literal_column("status") == "pendiente"
                    )
                )
            )
            orms = result.scalars().all()
            resers: list[Reservation] = []
            for orm in orms:
                v = self._map_orm_to_domain(orm=orm)
                resers.append(v)
            return Result.success(resers)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))
    
    async def get_all_by_date_restaurant(self, restaurant_id: str, reservation_date: date) -> Result[list[Reservation]]:
        try:
            result = await self.session.execute(
                select(OrmReservationModel).where(
                    and_(
                        literal_column("reservation_date") == reservation_date,
                        literal_column("restaurant_id") == restaurant_id,
                    )
                )
            )
            orms = result.scalars().all()
            resers: list[Reservation] = []
            for orm in orms:
                v = self._map_orm_to_domain(orm=orm)
                resers.append(v)
            return Result.success(resers)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))

    async def get_all(self) -> Result[list[Reservation]]:
        try:
            result = await self.session.execute(select(OrmReservationModel))
            orms = result.scalars().all()
            resers: list[Reservation] = []
            for orm in orms:
                v = self._map_orm_to_domain(orm=orm)
                resers.append(v)
            return Result.success(resers)
        except Exception as e:
            print(e,flush=True)
            return Result.fail(InfrastructureException(str(e)))
