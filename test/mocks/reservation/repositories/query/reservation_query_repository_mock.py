from datetime import date, time
from src.common.utils import Result
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository
from src.reservation.domain.aggregate.reservation import Reservation

class ReservationQueryRepositoryMock(IReservationQueryRepository):

    def __init__(self, main_data: list[Reservation]) -> None:
        self.main_data = main_data

    async def get_by_id(self, id: str) -> Result[Reservation]:
        res = next((u for u in self.main_data if u.id.reservation_id == id), None)
        if res:
            return Result.success(res)
        return Result.fail(Exception(""))

    async def exists_by_date_client(self, date_start: time, date_end: time, reservation_date: date, client_id: str) -> Result[bool]:
        res = next((u for u in self.main_data 
                    if u.date_start.reservation_date_start == date_start
                    and u.date_end.reservation_date_end == date_end
                    and u.date.reservation_date == reservation_date
                    and u.client_id.user_id == client_id
                    ), None)
        if res:
            return Result.success(True)
        return Result.success(False)

    async def exists_by_table(self, table_id: str, date_start: time, date_end: time, reservation_date: date, restaurant_id: str) -> Result[bool]:
        res = next((u for u in self.main_data 
                    if u.date_start.reservation_date_start == date_start
                    and u.date_end.reservation_date_end == date_end
                    and u.date.reservation_date == reservation_date
                    and u.restaurant_id.restaurant_id == restaurant_id
                    and u.table_number_id == table_id
                    ), None)
        if res:
            return Result.success(True)
        return Result.success(False)

    async def get_active_by_client_id(self, client_id: str) -> Result[list[Reservation]]:
        res = next((u for u in self.main_data if u.client_id.user_id == client_id), None)
        return Result.success(res)
        
    async def get_all_by_date_restaurant(self, restaurant_id: str, reservation_date: date,) -> Result[list[Reservation]]:
        res = next((u for u in self.main_data if 
                    u.restaurant_id.restaurant_id == restaurant_id
                    and u.date.reservation_date == reservation_date
                    ), None)
        return Result.success(res)
        
    async def get_all(self) -> Result[list[Reservation]]:
        return Result.success(self.main_data)
        