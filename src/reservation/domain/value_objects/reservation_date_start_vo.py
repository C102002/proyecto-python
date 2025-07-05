from datetime import time
from src.common.domain import ValueObjectRoot
from src.reservation.domain.domain_exceptions.invalid_reservation_date_start_exception import InvalidReservationDateStartException

class ReservationDateStartVo(ValueObjectRoot["ReservationDateStartVo"]):
    def __init__(self, reservation_date_start: time):
        if not isinstance(reservation_date_start, time):
            raise InvalidReservationDateStartException(reservation_date_start)

        if not (time.min <= reservation_date_start <= time.max):
            raise InvalidReservationDateStartException(str(reservation_date_start))

        self.__reservation_date_start = reservation_date_start

    def equals(self, value: "ReservationDateStartVo") -> bool:
        return self.__reservation_date_start == value.__reservation_date_start
    
    @property
    def reservation_date_start(self) -> time:
        return self.__reservation_date_start