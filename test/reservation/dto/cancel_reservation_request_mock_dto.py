from src.reservation.application.dtos.request.cancel_reservation_request_dto import CancelReservationRequest

class CancelReservationRequestMockDto(CancelReservationRequest):
    def __init__(self, client_id: str, reservation_id: str):
        self.client_id = client_id
        self.reservation_id = reservation_id