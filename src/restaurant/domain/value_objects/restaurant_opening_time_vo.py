from datetime import time
from src.common.domain import ValueObjectRoot
from src.restuarant.domain.domain_exceptions.invalid_opening_time_range_exception import InvalidOpeningTimeRangeException
from src.restuarant.domain.domain_exceptions.invalid_opening_time_exception import InvalidOpeningTimeRangeException


class RestaurantOpeningTimeVo(ValueObjectRoot["RestaurantOpeningTimeVo"]):
    def __init__(self, opening_time: time):

        if not isinstance(opening_time, time):
            raise InvalidOpeningTimeException(opening_time)

        if not (time.min <= opening_time <= time.max):
            raise InvalidOpeningTimeRangeException(str(opening_time))

        self.__opening_time = opening_time

    def equals(self, other: "RestaurantOpeningTimeVo") -> bool:
        return self.__opening_time == other.opening
    
    @property
    def opening_time(self) -> time:
        return self.opening_time