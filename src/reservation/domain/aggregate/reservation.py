from src.auth.domain.value_objects.user_id_vo import UserIdVo
from src.common.domain.domain_event.domain_event_root import DomainEventRoot
from src.common.domain import AggregateRoot
from src.menu.domain.entities.dish import Dish
from src.menu.domain.value_objects.dish_id_vo import DishIdVo
from src.menu.domain.value_objects.menu_id_vo import MenuIdVo
from src.reservation.domain.domain_exceptions.invalid_reservation_exception import InvalidReservationException
from src.reservation.domain.value_objects.reservation_date_end_vo import ReservationDateEndVo
from src.reservation.domain.value_objects.reservation_date_start_vo import ReservationDateStartVo
from src.reservation.domain.value_objects.reservation_date_vo import ReservationDateVo
from src.reservation.domain.value_objects.reservation_status_vo import ReservationStatusVo
from src.restaurant.domain.entities.value_objects.table_number_id_vo import TableNumberId
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo
from ..value_objects.reservation_id_vo import ReservationIdVo

class Reservation(AggregateRoot["ReservationIdVo"]):
    
    def __init__(
        self, 
        id: ReservationIdVo,
        date_end: ReservationDateEndVo,
        date_start: ReservationDateStartVo,
        reservation_date: ReservationDateVo,
        status: ReservationStatusVo,
        client_id: UserIdVo,
        table_number_id: TableNumberId,
        restaurant_id: RestaurantIdVo,
        dish: list[DishIdVo]
    ):
        super().__init__(id)
        self.__client_id = client_id
        self.__status = status
        self.__date_end = date_end
        self.__date_start = date_start
        self.__table_number_id = table_number_id
        self.__restaurant_id = restaurant_id
        self.__date = reservation_date
        self.__dish = dish
        self.validate_state()

    def when(self, event: DomainEventRoot) -> None:
        pass

    def validate_state(self) -> None:
        pass
    
    def update_status_pendiente(self) -> None:
        self.__status = ReservationStatusVo("pendiente")

    def update_status_confirmada(self) -> None:
        self.__status = ReservationStatusVo("confirmada")

    def update_status_cancelada(self) -> None:
        self.__status = ReservationStatusVo("cancelada")

    def update_status_completada(self) -> None:
        self.__status = ReservationStatusVo("completada")
    
    @property
    def date_start(self) -> ReservationDateStartVo:
        return self.__date_start

    @property
    def date(self) -> ReservationDateVo:
        return self.__date

    @property
    def date_end(self) -> ReservationDateEndVo:
        return self.__date_end

    @property
    def status(self) -> ReservationStatusVo:
        return self.__status

    @property
    def client_id(self) -> UserIdVo:
        return self.__client_id

    @property
    def restaurant_id(self) -> RestaurantIdVo:
        return self.__restaurant_id

    @property
    def table_number_id(self) -> TableNumberId:
        return self.__table_number_id

    @property
    def dish(self) -> list[Dish]:
        return self.__dish

    def update_dish(self, dish: list[DishIdVo]):
        self.__dish = dish