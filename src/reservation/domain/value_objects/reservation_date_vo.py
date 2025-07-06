from datetime import date
from src.common.domain import ValueObjectRoot
from src.reservation.domain.domain_exceptions.invalid_reservation_date_exception import InvalidReservationDateException

class ReservationDateVo(ValueObjectRoot["ReservationDateVo"]):
    def __init__(self, reservation_date: date):
        #if not isinstance(reservation_date, date):
        #    raise InvalidReservationDateException(reservation_date)

        #if (date.now() > reservation_date):
        #    raise InvalidReservationDateException(reservation_date)

        self.__reservation_date = reservation_date

    def equals(self, value: "ReservationDateVo") -> bool:
        return self.__reservation_date == value.__reservation_date
    
    @property
    def reservation_date_end(self) -> date:
        return self.__reservation_date