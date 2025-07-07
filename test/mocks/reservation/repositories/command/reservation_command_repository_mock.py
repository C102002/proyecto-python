from src.common.utils import Result
from src.auth.infrastructure.exceptions.user_not_found_exception import UserNotFoundException
from src.reservation.application.repositories.command.reservation_command_repository import IReservationCommandRepository
from src.reservation.domain.aggregate.reservation import Reservation

class ReservationCommandRepositoryMock(IReservationCommandRepository):
    
    def __init__(self, main_data: list[Reservation]) -> None:
        self.main_data = main_data

    async def save(self, entry: Reservation) -> Result[Reservation]:
        self.main_data.append(entry)
        return Result.success(entry)
    
    async def update(self, entry: Reservation) -> Result[Reservation]:
        for i, u in enumerate(self.user_store):
            if u.id == entry.id:
                self.main_data[i] = entry
                return Result.success(entry)
        return Result.fail(UserNotFoundException())
