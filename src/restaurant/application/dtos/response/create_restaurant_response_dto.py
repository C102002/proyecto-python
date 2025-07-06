from datetime import time
from typing import List, Optional

from src.restaurant.application.dtos.response.create_table_response_dto import CreateTableResponseDTO

class CreateRestaurantResponseDTO:
    def __init__(
        self,
        id: str,
        lat: float,
        lng: float,
        name: str,
        opening_time: time,
        closing_time: time,
        tables: Optional[List[CreateTableResponseDTO]] = None
    ):
        self.id = id
        self.lat = lat
        self.lng = lng
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.tables: List[CreateTableResponseDTO] = tables or []

    def __repr__(self):
        return (
            f"CreateRestaurantResponseDTO("
            f"id={self.id!r}, "
            f"lat={self.lat!r}, "
            f"lng={self.lng!r}, "
            f"name={self.name!r}, "
            f"opening_time={self.opening_time!r}, "
            f"closing_time={self.closing_time!r}, "
            f"tables={self.tables!r}"
            f")"
        )
