from datetime import time
from typing import List, Optional

from src.restaurant.application.dtos.request.create_table_request_dto import CreateTableRequestDTO



class CreateRestaurantRequestDTO:
    def __init__(
        self,
        lat: float,
        lng: float,
        name: str,
        opening_time: time,
        closing_time: time,
        tables: Optional[List[CreateTableRequestDTO]] = None,
    ):
        self.lat = lat
        self.lng = lng
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time
        # Si no se pasan tablas, inicializamos lista vacía
        self.tables: List[CreateTableRequestDTO] = tables or []

    def __repr__(self):
        return (
            f"CreateRestaurantRequestDTO("
            f"lat={self.lat!r}, "
            f"lng={self.lng!r}, "
            f"name={self.name!r}, "
            f"opening_time={self.opening_time!r}, "
            f"closing_time={self.closing_time!r}, "
            f"tables={self.tables!r}"
            f")"
        )
