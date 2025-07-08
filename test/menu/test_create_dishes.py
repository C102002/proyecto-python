import pytest
from fastapi import HTTPException
from src.menu.application.dtos.request.create_dish_request_dto import CreateDishRequestDto

@pytest.mark.asyncio
async def test_create_dishes_success(add_dish_to_menu_service):

    payload = CreateDishRequestDto(
        name="plato 1",
        restaurant_id="b8aac4b4-f340-451b-8e2f-9a5089bee6f9",
        category="Main",
        description="sdsdsd",
        image="sdasdasda",
        price=30
    )

    response = await add_dish_to_menu_service.execute(payload)

    assert response.is_success == True
    assert response.value.id is not None

@pytest.mark.asyncio
async def test_create_dishes_failure_by_name(add_dish_to_menu_service):

    payload1 = CreateDishRequestDto(
        name="plato 2",
        restaurant_id="b8aac4b4-f340-451b-8e2f-9a5089bee6f9",
        category="Main",
        description="sdsdsd",
        image="sdasdasda",
        price=30
    )

    response = await add_dish_to_menu_service.execute(payload1)

    payload2 = CreateDishRequestDto(
        name="plato 2",
        restaurant_id="b8aac4b4-f340-451b-8e2f-9a5089bee6f9",
        category="Main",
        description="sdsdsd",
        image="sdasdasda",
        price=50
    )

    status_code = 0

    try:
        response2 = await add_dish_to_menu_service.execute(payload2)
    except HTTPException as e:
        status_code = e.status_code
    
    assert status_code == 409