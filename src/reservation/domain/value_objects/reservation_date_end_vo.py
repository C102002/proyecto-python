from datetime import time
from src.common.domain import ValueObjectRoot
from src.reservation.domain.domain_exceptions.invalid_reservation_date_end_exception import InvalidReservationDateEndException

class ReservationDateEndVo(ValueObjectRoot["ReservationDateEndVo"]):
    def __init__(self, reservation_date_end: time):
        if not isinstance(reservation_date_end, time):
            raise InvalidReservationDateEndException(reservation_date_end)

        if not (time.min <= reservation_date_end <= time.max):
            raise InvalidReservationDateEndException(str(reservation_date_end))

        self.__reservation_date_end = reservation_date_end

    def equals(self, value: "ReservationDateEndVo") -> bool:
        return self.__reservation_date_end == value.__reservation_date_end
    
    @property
    def reservation_date_end(self) -> time:
        return self.__reservation_date_end