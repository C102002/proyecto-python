from typing import Optional
from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum

class CreateTableRequestDTO:
    def __init__(
        self,
        number: int,
        capacity: int,
        location: TableLocationEnum,
    ):
        """
        DTO para crear una mesa en un restaurante.

        :param number: Número identificador de la mesa.
        :param capacity: Capacidad máxima de comensales.
        :param location: Ubicación física de la mesa.
        :param restaurant_id: ID del restaurante (opcional si se anida).
        """
        self.number = number
        self.capacity = capacity
        self.location = location

    def __repr__(self):
        return (
            f"CreateTableRequestDTO("
            f"number={self.number!r}, "
            f"capacity={self.capacity!r}, "
            f"location={self.location!r}, "
            f")"
        )
