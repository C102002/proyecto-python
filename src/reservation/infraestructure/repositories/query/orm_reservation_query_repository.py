from datetime import date, time
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, select, literal_column
from src.auth.domain.value_objects.user_id_vo import UserIdVo
from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository
from src.reservation.domain.aggregate.reservation import Reservation
from src.reservation.domain.value_objects.reservation_date_end_vo import ReservationDateEndVo
from src.reservation.domain.value_objects.reservation_date_start_vo import ReservationDateStartVo
from src.reservation.domain.value_objects.reservation_id_vo import ReservationIdVo
from src.reservation.domain.value_objects.reservation_status_vo import ReservationStatusVo
from src.reservation.infraestructure.exceptions.reservation_not_found_exception import ReservationNotFoundException
from src.reservation.infraestructure.models.orm_reservation_model import OrmReservationModel

class OrmReservationQueryRepository(IReservationQueryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session
    
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
               Result.success(False)
            return Result.success(True)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))

    async def exists_by_table(self, table_id: str, date_start: time, date_end: time, reservation_date: date, ) -> Result[bool]:
        try:
            result = await self.session.execute(
                select(OrmReservationModel).where(
                    and_(
                        literal_column("table_number_id") == table_id,
                        literal_column("date_start") == date_start,
                        literal_column("date_end") == date_end,
                        literal_column("reservation_date") == reservation_date,
                    )
                )
            )
            oorm = result.scalars().first()
            if oorm is None:
               Result.success(False)
            return Result.success(True)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))

    async def get_active_by_client_id(self, client_id: str) -> Result[list[Reservation]]:
        try:
            result = await self.session.execute(
                select(OrmReservationModel).where(literal_column("client_id") == client_id)
            )
            orms = result.scalars().all()
            resers: list[Reservation] = []
            for orm in orms:
                v = Reservation(
                    client_id=(orm.id),
                    id=(orm.id),
                    date_end=(orm.date_end),
                    date_start=(orm.date_start),
                    reservation_date=(orm.reservation_date),
                    status=(orm.status),
                    table_number_id=(orm.table_number_id),
                    restaurant_id=orm.restaurant_id
                )
                resers.append(v)
            return Result.success(resers)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))
    
    async def get_all_by_date_restaurant(self, date_start: time, restaurant_id: str, reservation_date: date) -> Result[list[Reservation]]:
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
                v = Reservation(
                    client_id=(orm.id),
                    id=(orm.id),
                    date_end=(orm.date_end),
                    date_start=(orm.date_start),
                    reservation_date=(orm.reservation_date),
                    status=(orm.status),
                    table_number_id=(orm.table_number_id),
                    restaurant_id=orm.restaurant_id
                )
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
                v = Reservation(
                    client_id=(orm.id),
                    id=(orm.id),
                    date_end=(orm.date_end),
                    date_start=(orm.date_start),
                    reservation_date=(orm.reservation_date),
                    status=(orm.status),
                    table_number_id=(orm.table_number_id),
                    restaurant_id=orm.restaurant_id
                )
                resers.append(v)
            return Result.success(resers)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))
