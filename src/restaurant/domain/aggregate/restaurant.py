from src.common.domain.domain_event.domain_event_root import DomainEventRoot
from ...domain import AggregateRoot
from ...domain.domain_exceptions.invalid_restaurant_closing_greater_opening_exception import InvalidRestaurantClosingGreaterOpeningException
from ...domain.domain_exceptions.invalid_restaurant_exception import InvalidRestaurantException
from ...domain.value_objects.restaurant_closing_time_vo import RestaurantClosingTimeVo
from ...domain.value_objects.restaurant_id_vo import RestaurantIdVo
from ...domain.value_objects.restaurant_location_vo import RestaurantLocationVo
from ...domain.value_objects.restaurant_name_vo import RestaurantNameVo
from ...domain.value_objects.restaurant_opening_time_vo import RestaurantOpeningTimeVo


class Restaurant(AggregateRoot["RestaurantIdVo"]):
    
    def __init__(self, id: RestaurantIdVo, name: RestaurantNameVo, location: RestaurantLocationVo, opening_time: RestaurantOpeningTimeVo, closing_time: RestaurantClosingTimeVo):
        super().__init__(id)
        self.__location = location
        self.__name = name
        self.__opening_time = opening_time
        self.__closing_time = closing_time

    def when(self, event: DomainEventRoot) -> None:
        pass

    def validate_state(self) -> None:
        if not self._id or not self.__location or not self.__opening_time or not self.__closing_time:
            raise InvalidRestaurantException()
        
        if self.closing_time.closing_time > self.opening_time.opening_time:
            raise InvalidRestaurantClosingGreaterOpeningException(self.opening_time,self.closing_time)
        
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
    
    # TODO: Mesas creo que son entities