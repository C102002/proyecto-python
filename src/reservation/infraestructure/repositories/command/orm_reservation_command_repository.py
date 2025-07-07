from src.common.utils import Result
from src.common.infrastructure import InfrastructureException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from src.reservation.application.repositories.command.reservation_command_repository import IReservationCommandRepository
from src.reservation.domain.aggregate.reservation import Reservation
from src.reservation.infraestructure.exceptions.reservation_not_found_exception import ReservationNotFoundException
from src.reservation.infraestructure.models.orm_reservation_model import OrmReservationModel

class OrmReservationCommandRepository(IReservationCommandRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, entry: Reservation) -> Result[Reservation]:
        try:
            orm = OrmReservationModel(
                id=entry._id.reservation_id,
                date_end=entry.date_end.reservation_date_end,
                date_start=entry.date_start.reservation_date_start,
                status=entry.status.reservation_status,
                client_id=entry.client_id.user_id,
                table_number_id = entry.table_number_id.table_number_id,
                restaurant_id=entry.restaurant_id.restaurant_id,
                reservation_date=entry.date.reservation_date
            )
            self.session.add(orm)
            await self.session.commit()
            return Result.success(entry)
        except Exception as e:
            await self.session.rollback()
            err = InfrastructureException(str(e))
            return Result.fail(err)
        
    async def update(self, entry: Reservation) -> Result[Reservation]:
        try:
            stmt = select(OrmReservationModel).where(OrmReservationModel.id == entry._id)
            result = await self.session.execute(stmt)
            to_update = result.scalar_one_or_none()
            if to_update is None:
                err = ReservationNotFoundException()
                return Result.fail(err)
            to_update.status = entry.status.reservation_status
            self.session.add(to_update)
            await self.session.commit()
            return Result.success(entry)

        except Exception as e:
            await self.session.rollback()
            err = InfrastructureException(str(e))
            return Result.fail(err)