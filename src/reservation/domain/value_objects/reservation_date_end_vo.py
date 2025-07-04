from src.common.domain import ValueObjectRoot

class ReservationDateEndVo(ValueObjectRoot["ReservationDateEndVo"]):
    def __init__(self, reservation_date_end: str):
        # raise InvalDateEndReservationDateEndException(reservation_DateEnd)
        self.__reservation_date_end = reservation_date_end

    def equals(self, value: "ReservationDateEndVo") -> bool:
        return self.__reservation_date_end == value.__reservation_date_end
    
    @property
    def reservation_date_end(self) -> str:
        return self.__reservation_date_end