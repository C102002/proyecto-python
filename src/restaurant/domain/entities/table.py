from src.common.domain.domain_event.domain_event_root import DomainEventRoot
from src.common.domain.entity.entity_root import EntityRoot
from .domain_exceptions.invalid_table_exception import InvalidTableException
from .value_objects.table_capacity_vo import TableCapacityVo
from .value_objects.table_location_vo import TableLocationVo
from .value_objects.table_number_id_vo import TableNumberId

from ...domain.value_objects.restaurant_location_vo import RestaurantLocationVo


class Table(EntityRoot["TableNumberId"]):
    
    def __init__(self, id: TableNumberId, location: TableLocationVo, capacity:TableCapacityVo):
        super().__init__(id)
        self.__location = location
        self.__capacity = capacity

    def when(self, event: DomainEventRoot) -> None:
        pass

    def validate_state(self) -> None:
        if not self._id or not self.__location or not self.__capacity:
            raise InvalidTableException()
        
    def update_location(self, location: RestaurantLocationVo) -> None:
        self.__location = location
        self.validate_state()

    def update_capacity(self, capacity: TableCapacityVo) -> None:
        self.__capacity = capacity        
        self.validate_state()

    def update_number(self, number: TableNumberId) -> None:
        self._id = number        
        self.validate_state()

    @property
    def capacity(self) -> TableCapacityVo:
        return self.__capacity

    @property
    def location(self) -> TableLocationVo:
        return self.__location
    
    def __repr__(self):
        return (
            f"Table("
            f"id={self.id!r}, "
            f"capacity={self.capacity!r}, "
            f"location={self.location!r})"
        )
    