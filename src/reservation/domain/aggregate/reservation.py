from src.auth.domain.value_objects.user_id_vo import UserIdVo
from src.common.domain.domain_event.domain_event_root import DomainEventRoot
from src.common.domain import AggregateRoot
from src.reservation.domain.domain_exceptions.invalid_reservation_exception import InvalidReservationException
from src.reservation.domain.value_objects.reservation_date_end_vo import ReservationDateEndVo
from src.reservation.domain.value_objects.reservation_date_start_vo import ReservationDateStartVo
from src.reservation.domain.value_objects.reservation_status_vo import ReservationStatusVo
from ..value_objects.reservation_id_vo import ReservationIdVo

class Reservation(AggregateRoot["ReservationIdVo"]):
    
    def __init__(
        self, 
        id: ReservationIdVo,
        date_end: ReservationDateEndVo,
        date_start: ReservationDateStartVo,
        client_id: UserIdVo
    ):
        super().__init__(id)
        self.__client_id = client_id
        self.__status = ReservationStatusVo("pendiente")
        self.__date_end = date_end
        self.__date_start = date_start
        self.validate_state()

    def when(self, event: DomainEventRoot) -> None:
        pass

    def validate_state(self) -> None:
        if not self._id or not self.__client_id or not self.__date_end or not self.__date_start or not self.__status is None:
            raise InvalidReservationException()
        
        if self.__date_end.reservation_date_end < self.__date_start.reservation_date_start:
            raise InvalidReservationException()

    def update_status_pendiente(self) -> None:
        self.__status = ReservationStatusVo("pendiente")

    def update_status_confirmada(self) -> None:
        self.__status = ReservationStatusVo("confirmada")

    def update_status_cancelada(self) -> None:
        self.__status = ReservationStatusVo("cancelada")

    def update_status_completada(self) -> None:
        self.__status = ReservationStatusVo("completada")
        
    def update_date_end(self, date: ReservationDateEndVo) -> None:
        self.__date_end = date

    def update_date_start(self, date: ReservationDateStartVo) -> None:
        self.__date_start = date

    @property
    def date_start(self) -> ReservationDateStartVo:
        return self.__date_start

    @property
    def date_end(self) -> ReservationDateEndVo:
        return self.__date_end

    @property
    def status(self) -> ReservationStatusVo:
        return self.__status

    @property
    def cliend_id(self) -> UserIdVo:
        return self.cliend_id
