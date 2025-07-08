import pytest
import uuid
from src.restaurant.application.dtos.request.create_restaurant_request_dto import CreateRestaurantRequestDTO
from src.restaurant.application.dtos.request.create_table_dto import CreateTableDTO
from datetime import datetime
from fastapi import HTTPException
from src.restaurant.domain.entities.table import Table
from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum


@pytest.mark.asyncio
async def test_create_restaurant_success(create_restaurant_service):
    """
    GIVEN a valid payload for creating a restaurant
    WHEN POST /restaurant is called
    THEN it returns 201 and a body containing the new restaurant data
    """

    payload = CreateRestaurantRequestDTO(
        closing_time=datetime.strptime("22:00:00", "%H:%M:%S").time(),
        lat= -0.180653,
        lng= -78.467834,
        name="Mi Restaurante",
        opening_time=datetime.strptime("09:00:00", "%H:%M:%S").time(),
    )
    
    response = await create_restaurant_service.execute(payload)

    assert response.is_success == True

    # Verify that the response contains all expected fields
    assert response.value.id is not None
    assert uuid.UUID(response.value.id)  # valid UUID
    assert response.value.name == payload.name
    assert response.value.lat == pytest.approx(payload.lat, rel=1e-6)
    assert response.value.lng == pytest.approx(payload.lng, rel=1e-6)
    assert response.value.opening_time == payload.opening_time
    assert response.value.closing_time == payload.closing_time


# @pytest.mark.asyncio
# async def test_create_restaurant_missing_field():
#     """
#     GIVEN an invalid payload missing the 'name' field
#     WHEN POST /restaurant is called
#     THEN it returns 422 Unprocessable Entity with a validation error
#     """
#     payload = {
#         "lat": -0.180653,
#         "lng": -78.467834,
#         "opening_time": "08:00",
#         "closing_time": "22:00"
#     }

#     response = client.post("/restaurant", json=payload)
#     assert response.status_code == 422

#     data = response.json()
#     # FastAPI returns a list of validation errors under 'detail'
#     assert "detail" in data
#     assert any(err["loc"][-1] == "name" for err in data["detail"])


@pytest.mark.asyncio
async def test_create_restaurant_invalid_times(create_restaurant_service):
    """
    GIVEN a payload where closing_time is before opening_time
    WHEN POST /restaurant is called
    THEN it returns 400 Bad Request with a business validation error
    """

    payload = CreateRestaurantRequestDTO(
        closing_time=datetime.strptime("06:00:00", "%H:%M:%S").time(),
        lat= -0.180653,
        lng= -78.467834,
        name="Night Owl Lounge",
        opening_time=datetime.strptime("22:00:00", "%H:%M:%S").time(),
    )

    status_code = 0
    detail = ""

    try:
        response = await create_restaurant_service.execute(payload)
    except HTTPException as e:
        status_code = e.status_code
        detail = e.detail

    assert status_code == 400
    assert detail is not ""
    # Depending on implementation, you might check specific error message
    assert "invalid restaurant" in detail.lower() \
        and "opening time" in detail.lower() \
        and "closing time" in detail.lower()

@pytest.mark.asyncio
async def test_create_restaurant_invalid_min_capacity(create_restaurant_service):

    tables: list[CreateTableDTO] = []

    table = CreateTableDTO(
        number=1,
        capacity=1,
        location=TableLocationEnum.parque
    )
    tables.append(table)

    payload = CreateRestaurantRequestDTO(
        closing_time=datetime.strptime("22:00:00", "%H:%M:%S").time(),
        lat= -0.180653,
        lng= -78.467834,
        name="Mi Restaurante",
        opening_time=datetime.strptime("09:00:00", "%H:%M:%S").time(),
        tables=tables
    )

    status_code = 0

    try:
        response = await create_restaurant_service.execute(payload)
    except HTTPException as e:
        status_code = e.status_code
    
    assert status_code == 400

@pytest.mark.asyncio
async def test_create_restaurant_invalid_max_capacity(create_restaurant_service):

    tables: list[CreateTableDTO] = []

    table = CreateTableDTO(
        number=1,
        capacity=13,
        location=TableLocationEnum.parque
    )
    tables.append(table)

    payload = CreateRestaurantRequestDTO(
        closing_time=datetime.strptime("22:00:00", "%H:%M:%S").time(),
        lat= -0.180653,
        lng= -78.467834,
        name="Mi Restaurante",
        opening_time=datetime.strptime("09:00:00", "%H:%M:%S").time(),
        tables=tables
    )

    status_code = 0

    try:
        response = await create_restaurant_service.execute(payload)
    except HTTPException as e:
        status_code = e.status_code
    
    assert status_code == 400