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
    
    async def get_by_id(self, id: str) -> Result[Reservation]:
        try:
            result = await self.session.execute(
                select(OrmReservationModel).where(literal_column("id") == id)
            )
            orm = result.scalars().first()
            if orm is None:
                return Result.fail(ReservationNotFoundException())
            reser = Reservation( 
                id=ReservationIdVo(orm.id),
                status=ReservationStatusVo(orm.status),
                date_start=ReservationDateStartVo(orm.date_start),
                date_end=ReservationDateEndVo(orm.date_end),
                client_id=UserIdVo(orm.client_id)
            )
            return Result.success(reser)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))
        
    async def get_by_date(self, date_start: str, date_end: str) -> Result[Reservation]:
        try:
            result = await self.session.execute(
                select(OrmReservationModel).where(
                    and_(
                        literal_column("dateStart") == date_start,
                        literal_column("dateEnd") == date_end
                    )
                )
            )
            orm = result.scalars().first()
            if orm is None:
                return Result.fail(ReservationNotFoundException())
            reser = Reservation( 
                id=ReservationIdVo(orm.id),
                status=ReservationStatusVo(orm.status),
                date_start=ReservationDateStartVo(orm.date_start),
                date_end=ReservationDateEndVo(orm.date_end),
                client_id=UserIdVo(orm.client_id)
            )
            return Result.success(reser)
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
                    status=(orm.status)
                )
                resers.append(v)
            return Result.success(resers)
        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))

    async def get_all_by_date_restaurant(self) -> Result[list[Reservation]]:
        pass

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
                    status=(orm.status)
                )
                resers.append(v)

            return Result.success(resers)

        except Exception as e:
            return Result.fail(InfrastructureException(str(e)))
