from typing import Optional
from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum

class UpdateTableRequestDTO:
    def __init__(
        self,
        restaurant_id: str,
        number: int,
        new_number: Optional[int] = None,
        capacity: Optional[int] = None,
        location: Optional[TableLocationEnum] = None,
    ):
        """
        DTO for updating a table in a restaurant.
        You must supply:
          - restaurant_id: UUID of the restaurant
          - number: current table identifier

        Optionally supply:
          - new_number: new table identifier
          - capacity: new seating capacity
          - location: new physical location
        """
        self.restaurant_id = restaurant_id
        self.number = number
        self.new_number = new_number
        self.capacity = capacity
        self.location = location

    def __repr__(self):
        return (
            f"UpdateTableRequestDTO("
            f"restaurant_id={self.restaurant_id!r}, "
            f"number={self.number!r}, "
            f"new_number={self.new_number!r}, "
            f"capacity={self.capacity!r}, "
            f"location={self.location!r}"
            f")"
        )
