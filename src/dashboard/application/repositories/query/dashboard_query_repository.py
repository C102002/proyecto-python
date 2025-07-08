from abc import ABC, abstractmethod
from typing import List

from src.common.utils.result import Result
from src.dashboard.application.dtos.request.get_reservation_count_request_dto import GetReservationCountRequestDTO
from src.dashboard.application.dtos.response.get_occupacy_percentage_response_dto import GetOccupancyPercentageResponseDto
from src.dashboard.application.dtos.request.get_occupacy_percentage_request_dto import GetOccupancyPercentageRequestDto
from src.dashboard.application.dtos.response.get_top_dishes_preorder_response_dto import GetTopDishesPreorderRequestDTO
from src.dashboard.application.dtos.request.get_top_dishes_preorder_request_dto import GetTopDishesPreorderRequestDTO
from src.dashboard.application.dtos.response.get_reservation_count_response_dto import GetReservationCountResponseDTO

class IDashboardQueryRepository(ABC):
    """
    Repositorio que expone los tres queries de dashboard para el 
    administrador.
    """

    @abstractmethod
    async def get_reservations_count(self, dto:GetReservationCountRequestDTO) -> Result[GetReservationCountResponseDTO]:
        pass

    @abstractmethod
    async def get_top_preordered_dishes(
        self,
        dto:GetTopDishesPreorderRequestDTO
    ) -> Result[List[GetTopDishesPreorderRequestDTO]]:
        """
        returns  `top_n` disher preordered.
        """
        pass

    @abstractmethod
    async def get_occupancy_percentage_by_restaurant(
        self,
        dto:GetOccupancyPercentageRequestDto
    ) -> Result[List[GetOccupancyPercentageResponseDto]]:
        """
        Occupancy percentage per restaurant for a specific month.
        """
        raise NotImplementedError
