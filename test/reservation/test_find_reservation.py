import pytest
from src.reservation.application.dtos.request.find_reservation_request_dto import FindReservationRequest

@pytest.mark.asyncio
async def test_reservation_find_success(service):
    request = FindReservationRequest()
    response = await service.execute(request)
    assert response.status_code == 200
    