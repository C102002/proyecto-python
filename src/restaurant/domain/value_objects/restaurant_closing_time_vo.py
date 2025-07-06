from datetime import time
from src.common.domain import ValueObjectRoot
from ...domain.domain_exceptions.invalid_closing_time_exception import InvalidClosingTimeException
from ...domain.domain_exceptions.invalid_closing_time_range_exception import InvalidClosingTimeRangeException


class RestaurantClosingTimeVo(ValueObjectRoot["RestaurantClosingTimeVo"]):
    def __init__(self, closing_time: time):

        if not isinstance(closing_time, time):
            raise InvalidClosingTimeException(closing_time)

        if not (time.min <= closing_time <= time.max):
            raise InvalidClosingTimeRangeException(str(closing_time))

        self.__closing_time = closing_time

    def equals(self, other: "RestaurantClosingTimeVo") -> bool:
        return self.__closing_time == other.closing_time
    
    @property
    def closing_time(self) -> time:
        return self.__closing_time