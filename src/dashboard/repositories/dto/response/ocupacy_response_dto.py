from typing import NamedTuple


class OccupancyResponseDTO(NamedTuple):
    """
    % de ocupación por restaurante en un periodo dado.
    """
    restaurant_id: str
    restaurant_name: str
    occupied_tables: int
    total_tables: int
    occupancy_percent: float  # occupied_tables/total_tables * 100