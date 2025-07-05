from abc import ABC, abstractmethod
import time
from src.common.utils import Result
from src.reservation.domain.aggregate.reservation import Reservation

class IReservationQueryRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: str) -> Result[Reservation]:
        pass

    @abstractmethod
    async def exists_by_date_client(self, date_start: time, date_end: time) -> Result[bool]:
        pass

    @abstractmethod
    async def exists_by_table(self, table_id: str, date_start: time, date_end: time) -> Result[bool]:
        pass

    @abstractmethod
    async def get_active_by_client_id(self, client_id: str) -> Result[list[Reservation]]:
        pass

    @abstractmethod
    async def get_all_by_date_restaurant(self, date_start: time, restaurant_id) -> Result[list[Reservation]]:
        pass

    @abstractmethod
    async def get_all(self) -> Result[list[Reservation]]:
        pass
