from datetime import time 
from src.common.domain import ValueObjectRoot
from ...domain.domain_exceptions.invalid_opening_time_range_exception import InvalidOpeningTimeRangeException
from ...domain.domain_exceptions.invalid_opening_time_exception import InvalidOpeningTimeException



class RestaurantOpeningTimeVo(ValueObjectRoot["RestaurantOpeningTimeVo"]):
    def __init__(self, opening_time: time):

        if not isinstance(opening_time, time):
            raise InvalidOpeningTimeException(opening_time)

        if opening_time.tzinfo is not None:
            raise InvalidOpeningTimeException(
                f"{opening_time.tzinfo}"
            )

        if not (time.min <= opening_time <= time.max):
            raise InvalidOpeningTimeRangeException(str(opening_time))

        self._opening_time = opening_time

    def equals(self, other: "RestaurantOpeningTimeVo") -> bool:
        return self._opening_time == other._opening_time

    @property
    def opening_time(self) -> time:
        return self._opening_time
