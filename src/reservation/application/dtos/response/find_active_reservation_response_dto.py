
from src.reservation.domain.aggregate.reservation import Reservation


class FindActiveReservationResponse:
    def __init__(self, reservations: list[Reservation]):
        self.reservations = reservations