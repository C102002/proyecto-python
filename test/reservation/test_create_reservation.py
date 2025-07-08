import pytest
from src.reservation.application.dtos.request.create_reservation_request_dto import CreateReservationRequest
from src.restaurant.application.dtos.request.create_restaurant_request_dto import CreateRestaurantRequestDTO
from src.menu.application.dtos.request.create_dish_request_dto import CreateDishRequestDto
from src.restaurant.application.dtos.request.create_table_dto import CreateTableDTO
from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum
from datetime import datetime
from fastapi import HTTPException

@pytest.mark.asyncio
async def test_reservation_create_success(create_reservation_service, create_restaurant_service, add_dish_to_menu_service):

    tables: list[CreateTableDTO] = []

    table = CreateTableDTO(
        number=1,
        capacity=5,
        location=TableLocationEnum.parque
    )
    tables.append(table)

    payload = CreateRestaurantRequestDTO(
        closing_time=datetime.strptime("22:00:00", "%H:%M:%S").time(),
        lat= -0.180653,
        lng= -78.467834,
        name="Restaurante test",
        opening_time=datetime.strptime("09:00:00", "%H:%M:%S").time(),
        tables=tables
    )
    
    response = await create_restaurant_service.execute(payload)
    
    request_menu = CreateDishRequestDto(
        category="Main",
        description="dsfdsf",
        image="fFffs",
        name="plato test",
        price=40,
        restaurant_id=response.value.id
    )

    response_menu = await add_dish_to_menu_service.execute(request_menu)

    request = CreateReservationRequest(
        client_id="197dd255-a202-4aed-b973-bc7af39ee411",
        date_start=datetime.strptime("00:46:53", "%H:%M:%S").time(),
        date_end=datetime.strptime("02:46:53", "%H:%M:%S").time(),
        reservation_date=datetime.strptime("2025-07-07", "%Y-%m-%d").date(),
        table_number_id=response.value.tables[0].id,
        restaurant_id=response.value.id,
        dish_id=[response_menu.value.id.value]
    )

    response = await create_reservation_service.execute(request)
    
    assert response.is_success == True

    assert response.value.id is not None

@pytest.mark.asyncio
async def test_reservation_create_failed_by_reservation_time_table(create_reservation_service, create_restaurant_service, add_dish_to_menu_service):

    tables: list[CreateTableDTO] = []

    table = CreateTableDTO(
        number=1,
        capacity=5,
        location=TableLocationEnum.parque
    )
    tables.append(table)

    payload = CreateRestaurantRequestDTO(
        closing_time=datetime.strptime("22:00:00", "%H:%M:%S").time(),
        lat= -0.180653,
        lng= -78.467834,
        name="Restaurante test 2",
        opening_time=datetime.strptime("09:00:00", "%H:%M:%S").time(),
        tables=tables
    )
    
    response = await create_restaurant_service.execute(payload)
    
    request_menu = CreateDishRequestDto(
        category="Main",
        description="dsfdsf",
        image="fFffs",
        name="plato test 2",
        price=40,
        restaurant_id=response.value.id
    )

    response_menu = await add_dish_to_menu_service.execute(request_menu)
    
    request1 = CreateReservationRequest(
        client_id="197dd255-a202-4aed-b973-bc7af39ee417",
        date_start=datetime.strptime("00:46:53", "%H:%M:%S").time(),
        date_end=datetime.strptime("02:46:53", "%H:%M:%S").time(),
        reservation_date=datetime.strptime("2025-07-07", "%Y-%m-%d").date(),
        table_number_id=response.value.tables[0].id,
        restaurant_id=response.value.id,
        dish_id=[response_menu.value.id.value]
    )

    request2 = CreateReservationRequest(
        client_id="197dd255-a202-4aed-b973-bc7af39ee417",
        date_start=datetime.strptime("00:46:53", "%H:%M:%S").time(),
        date_end=datetime.strptime("02:46:53", "%H:%M:%S").time(),
        reservation_date=datetime.strptime("2025-07-07", "%Y-%m-%d").date(),
        table_number_id=response.value.tables[0].id,
        restaurant_id=response.value.id,
        dish_id=[response_menu.value.id.value]
    )

    response1 = await create_reservation_service.execute(request1)
    
    assert response1.is_success == True

    assert response1.value.id is not None

    status_code = 0

    try:
        response2 = await create_reservation_service.execute(request2)
    except HTTPException as e:
        status_code = e.status_code
    
    assert status_code == 409


@pytest.mark.asyncio
async def test_reservation_create_failed_by_dish(create_reservation_service, create_restaurant_service, add_dish_to_menu_service):

    tables: list[CreateTableDTO] = []

    table = CreateTableDTO(
        number=1,
        capacity=5,
        location=TableLocationEnum.parque
    )
    tables.append(table)

    payload = CreateRestaurantRequestDTO(
        closing_time=datetime.strptime("22:00:00", "%H:%M:%S").time(),
        lat= -0.180653,
        lng= -78.467834,
        name="Restaurante test 3",
        opening_time=datetime.strptime("09:00:00", "%H:%M:%S").time(),
        tables=tables
    )
    
    response = await create_restaurant_service.execute(payload)
    
    request1 = CreateReservationRequest(
        client_id="197dd255-a202-4aed-b973-bc7af39ee418",
        date_start=datetime.strptime("00:46:53", "%H:%M:%S").time(),
        date_end=datetime.strptime("02:46:53", "%H:%M:%S").time(),
        reservation_date=datetime.strptime("2025-07-07", "%Y-%m-%d").date(),
        table_number_id=response.value.tables[0].id,
        restaurant_id=response.value.id,
        dish_id=["197dd255-a202-4aed-b973-bc7af39ee438"]
    )

    status_code = 0

    try:
        response1 = await create_reservation_service.execute(request1)
    except HTTPException as e:
        status_code = e.status_code
    
    assert status_code == 400