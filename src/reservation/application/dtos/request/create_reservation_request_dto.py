
class CreateReservationRequest:
    def __init__(self, client_id: str, date_start: str, date_end: str):
        self.client_id = client_id
        self.date_start = date_start
        self.date_end = date_end
