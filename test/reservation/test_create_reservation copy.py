import pytest
from src.reservation.application.dtos.request.create_reservation_request_dto import CreateReservationRequest

@pytest.mark.asyncio
async def test_reservation_create_success(service):
    request = CreateReservationRequest(
        client_id = "197dd255-a202-4aed-b973-bc7af39ee411",
        date_start = "00:46:53.358Z",
        date_end = "02:46:53.358Z",
        reservation_date = "2025-07-07",
        table_number_id = "4ac95fe2-2879-445c-b3a1-bb136be2ab2a",
        restaurant_id = "4ac95fe2-2879-445c-b3a1-bb136be2ab2a",
        dish_id = ["4ac95fe2-2879-445c-b3a1-bb136be2ab2a"]
    )
    response = await service.execute(request)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data is None
    