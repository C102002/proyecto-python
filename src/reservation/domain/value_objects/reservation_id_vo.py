from src.common.domain import ValueObjectRoot
import uuid

from src.reservation.domain.domain_exceptions.invalid_reservation_id_exception import InvalidReservationIdException

class ReservationIdVo(ValueObjectRoot["ReservationIdVo"]):
    def __init__(self, reservation_id: str):
        try:
            uuid.UUID(reservation_id)
        except ValueError:
            raise InvalidReservationIdException(reservation_id)
        
        self.__reservation_id = reservation_id

    def equals(self, value: "ReservationIdVo") -> bool:
        return self.__reservation_id == value.__reservation_id
    
    @property
    def reservation_id(self) -> str:
        return self.__reservation_id