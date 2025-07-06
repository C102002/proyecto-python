from enum import Enum
from src.common.domain import ValueObjectRoot
from src.restaurant.domain.entities.domain_exceptions.invalid_table_location_name import InvalidTableLocationNameException
from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum


class TableLocationVo(ValueObjectRoot["TableLocationVo"]):

    def __init__(self, location: str):
        if isinstance(location, str):
            try:
                location_enum = TableLocationEnum(location.strip().lower())
            except ValueError:
                raise InvalidTableLocationNameException(f"{location!r}")
        self._location = location_enum

    def equals(self, other: "TableLocationVo") -> bool:
        return self._location is other._location

    @property
    def location(self) -> TableLocationEnum:
        return self._location

    def __repr__(self) -> str:
        return f"TableLocationVo({self._location.value!r})"
