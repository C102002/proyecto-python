import pytest
from src.reservation.application.dtos.request.find_active_reservation_request_dto import FindActiveReservationRequest

@pytest.mark.asyncio
async def test_reservation_find_active_success(service):
    request = FindActiveReservationRequest(
        client_id="197dd255-a202-4aed-b973-bc7af39ee411"
    )
    response = await service.execute(request)
    assert response.status_code == 200
    