from datetime import datetime
from typing import List

from src.reservation.domain.aggregate.reservation import Reservation

# DTO para una sola reservación con tipos primitivos
class ActiveReservationResponse:
    def __init__(
        self,
        id: str,
        client_id: str,
        date_start: datetime,
        date_end: datetime,
        reservation_date: datetime,
        status: str,
        table_number_id: int,
        restaurant_id: str,
        dishes: List[str]
    ):
        self.id = id
        self.client_id = client_id
        self.date_start = date_start
        self.date_end = date_end
        self.reservation_date = reservation_date
        self.status = status
        self.table_number_id = table_number_id
        self.restaurant_id = restaurant_id
        self.dishes = dishes

    @classmethod
    def from_domain(cls, r: Reservation) -> "ActiveReservationResponse":
        return cls(
            id=r.id.reservation_id,
            client_id=r.client_id.user_id,
            date_start=r.date_start.reservation_date_start,
            date_end=r.date_end.reservation_date_end,
            reservation_date=r.date.reservation_date,
            status=r.status.reservation_status,
            table_number_id=r.table_number_id.table_number_id,
            restaurant_id=r.restaurant_id.restaurant_id,
            dishes=[d._id.__value for d in r.dish]
        )

# Wrapper que recibe la lista de agregados y expone solo primitivos
class FindActiveReservationResponse:
    def __init__(self, reservations: List[Reservation]):
        self.reservations: List[ActiveReservationResponse] = [
            ActiveReservationResponse.from_domain(r) for r in reservations
        ]
