from abc import ABC, abstractmethod
from datetime import date
import time
from src.common.utils import Result
from src.reservation.domain.aggregate.reservation import Reservation

class IReservationQueryRepository(ABC):

    @abstractmethod
    async def exists_by_date_client(self, date_start: time, date_end: time, reservation_date: date, client_id: str) -> Result[bool]:
        pass

    @abstractmethod
    async def exists_by_table(self, table_id: str, date_start: time, date_end: time, reservation_date: date,) -> Result[bool]:
        pass

    @abstractmethod
    async def get_active_by_client_id(self, client_id: str) -> Result[list[Reservation]]:
        pass

    @abstractmethod
    async def get_all_by_date_restaurant(self, restaurant_id: str, reservation_date: date,) -> Result[list[Reservation]]:
        pass

    @abstractmethod
    async def get_all(self) -> Result[list[Reservation]]:
        pass
