from abc import ABC, abstractmethod
from src.common.utils import Result
from src.reservation.domain.aggregate.reservation import Reservation

class IReservationQueryRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: str) -> Result[Reservation]:
        pass

    @list[abstractmethod]
    async def get_active_by_client_id(self, client_id: str) -> Result[list[Reservation]]:
        pass

    @abstractmethod
    async def get_all_by_date_restaurant(self) -> Result[list[Reservation]]:
        pass

    @abstractmethod
    async def get_all(self) -> Result[list[Reservation]]:
        pass
