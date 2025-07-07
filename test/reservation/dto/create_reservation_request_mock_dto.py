
from src.reservation.application.dtos.request.create_reservation_request_dto import CreateReservationRequest

from datetime import time, date

class UserRegisterRequestMockDto(CreateReservationRequest):
    def __init__(self, client_id: str, date_start: time, date_end: time, reservation_date: date, restaurant_id: str, table_number_id: str, dish_id: list[str]):
        self.client_id = client_id
        self.date_start = date_start
        self.date_end = date_end
        self.reservation_date = reservation_date
        self.table_number_id = table_number_id
        self.restaurant_id = restaurant_id
        self.dish_id = dish_id
