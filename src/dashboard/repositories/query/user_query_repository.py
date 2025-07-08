from abc import ABC, abstractmethod
from typing import List
from datetime import date

class DashboardQueryRepository(ABC):
    """
    Repositorio que expone los tres queries de dashboard para el 
    administrador.
    """

    @abstractmethod
    async def get_reservations_count_by_day(self) -> List[ReservationCountDTO]:
        """
        Total de reservas por día.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_reservations_count_by_week(self) -> List[ReservationCountDTO]:
        """
        Total de reservas por semana.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_top_preordered_dishes(
        self,
        top_n: int = 5
    ) -> List[DishPreorderDTO]:
        """
        Devuelve los `top_n` platos más pre-ordenados.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_occupancy_percentage_by_restaurant(
        self,
        month: int,
        year: int
    ) -> List[OccupancyDTO]:
        """
        % de ocupación por restaurante en un mes concreto.
        """
        raise NotImplementedError
