from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum

class CreateTableRequestDTO:
    def __init__(
        self,
        number: int,
        capacity: int,
        location: TableLocationEnum,
    ):
        """
        DTO for creating a table in a restaurant.

        :param number: Table identifier number.
        :param capacity: Maximum number of diners the table can seat.
        :param location: Physical location of the table.
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
