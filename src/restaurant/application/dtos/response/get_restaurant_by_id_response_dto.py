from datetime import time
from typing import List

from src.restaurant.application.dtos.response.create_table_response_dto import CreateTableResponseDTO


class GetRestaurantByIdResponseDTO:
    def __init__(
        self,
        id: str,
        lat: float,
        lng: float,
        name: str,
        opening_time: time,
        closing_time: time,
        tables: List[CreateTableResponseDTO] = None
    ):
        """
        DTO de respuesta para obtener un restaurante por ID.

        :param id: UUID único del restaurante
        :param lat: Latitud en grados decimales
        :param lng: Longitud en grados decimales
        :param name: Nombre del restaurante
        :param opening_time: Hora de apertura (HH:MM:SS)
        :param closing_time: Hora de cierre (HH:MM:SS)
        :param tables: Lista de mesas asociadas al restaurante
        """
        self.id = id
        self.lat = lat
        self.lng = lng
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.tables = tables or []

    def __repr__(self):
        return (
            f"GetRestaurantByIdResponseInfDTO("
            f"id={self.id!r}, "
            f"lat={self.lat!r}, "
            f"lng={self.lng!r}, "
            f"name={self.name!r}, "
            f"opening_time={self.opening_time!r}, "
            f"closing_time={self.closing_time!r}, "
            f"tables={self.tables!r}"
            f")"
        )
