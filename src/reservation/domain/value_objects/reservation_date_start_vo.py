from src.common.domain import ValueObjectRoot

class ReservationDateStartVo(ValueObjectRoot["ReservationDateStartVo"]):
    def __init__(self, reservation_date_start: str):
        #raise InvalDatestartReservationDatestartException(reservation_Datestart)
        self.__reservation_date_start = reservation_date_start

    def equals(self, value: "ReservationDateStartVo") -> bool:
        return self.__reservation_date_start == value.__reservation_date_start
    
    @property
    def reservation_date_start(self) -> str:
        return self.__reservation_date_start