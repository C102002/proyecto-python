from src.common.domain import DomainException
from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum

class InvalidTableLocationNameException(DomainException):

    def __init__(self, name: str):
        valid_values = [e.value for e in TableLocationEnum]
        message = (
            f"Invalid table location '{name}'. "
            f"Must be one of: {', '.join(valid_values)}."
        )
        super().__init__(message)