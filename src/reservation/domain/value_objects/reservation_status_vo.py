from src.common.domain import ValueObjectRoot
from src.reservation.domain.domain_exceptions.invalid_reservation_status_exception import InvalidReservationStatusException

class ReservationStatusVo(ValueObjectRoot["ReservationStatusVo"]):
    PENDIENTE = "pendiente"
    COMPLETADA = "completada"
    CANCELADA = "cancelada"
    CONFIRMADA = "confirmada"

    ESTADOS_VALIDOS = {PENDIENTE, COMPLETADA, CANCELADA, CONFIRMADA}
    
    def __init__(self, reservation_status: str):
        if reservation_status not in self.ESTADOS_VALIDOS:
            raise InvalidReservationStatusException(reservation_status)
        self.__reservation_status = reservation_status

    def equals(self, value: "ReservationStatusVo") -> bool:
        return self.__reservation_status == value.__reservation_status
    
    @property
    def reservation_status(self) -> str:
        return self.__reservation_status