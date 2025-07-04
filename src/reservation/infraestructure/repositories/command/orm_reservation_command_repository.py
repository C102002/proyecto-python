from src.auth.infrastructure.models.orm_user_model import OrmUserModel
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
            orm = OrmUserModel(
                id=id,
                dateEnd=entry.date_end.reservation_date_end,
                dateStart=entry.date_start.reservation_date_start,
                status=entry.status.reservation_status,
                clientID=entry.__client_id.user_id
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
            
            stmt = select(OrmReservationModel).where(OrmReservationModel.id == entry.id.reservation_id)
            result = await self.session.execute(stmt)
            to_update = result.scalar_one_or_none()

            if to_update is None:
                err = ReservationNotFoundException()
                return Result.fail(err)

            to_update.dateStart = entry.date_start
            to_update.dateEnd = entry.date_end
            to_update.status = entry.status
            
            self.session.add(to_update)
            await self.session.commit()
            return Result.success(entry)

        except Exception as e:
            await self.session.rollback()
            err = InfrastructureException(str(e))
            return Result.fail(err)