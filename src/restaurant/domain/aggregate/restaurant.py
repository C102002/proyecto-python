from typing import List
from src.common.domain.domain_event.domain_event_root import DomainEventRoot
from src.common.domain import AggregateRoot
from src.restaurant.domain.domain_exceptions.invalid_restaurant_delete_exception import InvalidRestaurantDeleteException
from src.restaurant.domain.domain_exceptions.invalid_table_delete_exception import InvalidTableDeleteException
from src.restaurant.domain.domain_exceptions.invalid_table_number_id import InvalidTableNumberIdException
from src.restaurant.domain.entities.table import Table
from src.restaurant.domain.entities.value_objects.table_number_id_vo import TableNumberId
from ...domain.domain_exceptions.invalid_restaurant_closing_greater_opening_exception import InvalidRestaurantClosingGreaterOpeningException
from ...domain.domain_exceptions.invalid_restaurant_exception import InvalidRestaurantException
from ...domain.value_objects.restaurant_closing_time_vo import RestaurantClosingTimeVo
from ...domain.value_objects.restaurant_id_vo import RestaurantIdVo
from ...domain.value_objects.restaurant_location_vo import RestaurantLocationVo
from ...domain.value_objects.restaurant_name_vo import RestaurantNameVo
from ...domain.value_objects.restaurant_opening_time_vo import RestaurantOpeningTimeVo


class Restaurant(AggregateRoot["RestaurantIdVo"]):
    
    def __init__(self, id: RestaurantIdVo, name: RestaurantNameVo, location: RestaurantLocationVo, opening_time: RestaurantOpeningTimeVo, closing_time: RestaurantClosingTimeVo, tables: List[Table]=[]):
        super().__init__(id)
        self.__location = location
        self.__name = name
        self.__opening_time = opening_time
        self.__closing_time = closing_time
        self.__tables = tables
        
        self.validate_state()

    def when(self, event: DomainEventRoot) -> None:
        pass

    def validate_state(self) -> None:
        if not self._id or not self.__location or not self.__opening_time or not self.__closing_time or self.__tables is None:
            raise InvalidRestaurantException()
        
        if self.closing_time.closing_time <= self.opening_time.opening_time:
            raise InvalidRestaurantClosingGreaterOpeningException(self.opening_time.opening_time,self.closing_time.closing_time)
        
    def update_location(self, location: RestaurantLocationVo) -> None:
        self.__location = location

    def update_name(self, name: RestaurantNameVo) -> None:
        self.__name = name

    def update_opening_time(self, opening_time: RestaurantOpeningTimeVo) -> None:
        self.__opening_time = opening_time
        self.validate_state()
        
    def update_closing_time(self, closing_time: RestaurantClosingTimeVo) -> None:
        self.__closing_time = closing_time
        self.validate_state()
    
    def add_table(self, table:Table) -> None:
        for domain_table in self.__tables:
            #! domain_table.equals(table) OJO ESTE NO ME DA IGUAL que equals del id, ahi si me funciono
            if domain_table.id.equals(table.id):
                raise InvalidTableNumberIdException(table.id.table_number_id)
                
        self.__tables.append(table)
        self.validate_state()
        
    def delete_table(self, table_id: TableNumberId) -> Table:
        """
        Remove the given table from this restaurant.
        Raises InvalidTableNumberIdException if not found.
        """
        # Try to find the table in the list
        for idx, domain_table in enumerate(self.__tables):
            if domain_table.id.equals(table_id):
                # Remove it and re-validate the aggregate
                table_delete = self.__tables.pop(idx)
                self.validate_state()
                return table_delete
        raise InvalidTableDeleteException(table_id.table_number_id)
        
    def delete(self) -> None:
        if len(self.tables) != 0:            
            raise InvalidRestaurantDeleteException(len(self.tables))
        self.validate_state()

        
    @property
    def name(self) -> RestaurantNameVo:
        return self.__name

    @property
    def location(self) -> RestaurantLocationVo:
        return self.__location
    
    @property
    def opening_time(self) -> RestaurantOpeningTimeVo:
        return self.__opening_time
    
    @property
    def closing_time(self) -> RestaurantClosingTimeVo:
        return self.__closing_time
    
    @property
    def tables(self) -> List[Table]:
        return self.__tables
    
    # TODO: Mesas creo que son entities