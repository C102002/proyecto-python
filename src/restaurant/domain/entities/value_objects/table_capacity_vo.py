from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_table_capacity_exception import InvalidTableCapacity

class TableCapacityVo(ValueObjectRoot["TableCapacityVo"]):
    def __init__(self, capacity: int):
        
        # Valida rango permitido: [2, 12]
        if capacity < 2 or capacity > 12:
            raise InvalidTableCapacity(capacity=capacity)

        self.__capacity = capacity

    def equals(self, other: "TableCapacityVo") -> bool:
        return self.__capacity == other.capacity
    
    @property
    def capacity(self) -> int:
        return self.__capacity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(capacity={self.__capacity})"
