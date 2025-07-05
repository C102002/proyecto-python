
from datetime import time, date
class CreateReservationRequest:
    def __init__(self, client_id: str, date_start: time, date_end: time, reservation_date: date):
        self.client_id = client_id
        self.date_start = date_start
        self.date_end = date_end
        self.reservation_date = reservation_date
