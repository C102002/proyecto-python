from src.common.domain import ValueObjectRoot

class ReservationStatusVo(ValueObjectRoot["ReservationStatusVo"]):
    def __init__(self, reservation_status: str):
        # PENDIENTE = "pendiente"
        # COMPLETADA = "completada"
        # CANCELADA = "cancelada"
        # CONFIRMADA = "confirmada"
        
        # raise InvalidReservationStatusException(reservation_Status)
        self.__reservation_status = reservation_status

    def equals(self, value: "ReservationStatusVo") -> bool:
        return self.__reservation_status == value.__reservation_status
    
    @property
    def reservation_status(self) -> str:
        return self.__reservation_status