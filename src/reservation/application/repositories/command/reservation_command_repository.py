from abc import ABC, abstractmethod
from typing import List
from src.common.utils import Result
from src.reservation.domain.aggregate.reservation import Reservation

class IReservationCommandRepository(ABC):
    @abstractmethod
    async def save(self, entry: Reservation) -> Result[Reservation]:
        pass

    @abstractmethod
    async def update(self, entry: Reservation) -> Result[Reservation]:
        pass
    
    