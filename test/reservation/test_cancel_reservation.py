import pytest
from src.reservation.application.dtos.request.cancel_reservation_request_dto import CancelReservationRequest

@pytest.mark.asyncio
async def test_reservation_cancel_success(service):
    request = CancelReservationRequest(
        client_id = "197dd255-a202-4aed-b973-bc7af39ee411",
        reservation_id = "197dd255-a202-4aed-b973-bc7af39ee412"
    )
    response = await service.execute(request)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data is None
    