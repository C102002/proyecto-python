from fastapi import APIRouter, Depends, HTTPException
from src.menu.application.dtos.request.create_dish_request_dto import CreateDishRequestDto
from src.menu.application.dtos.response.dish_response_dto import DishResponseDto
from src.menu.application.services.menu_service import MenuService
from src.menu.infrastructure.dependencies import get_menu_service

router = APIRouter()

@router.post("/dishes/{restaurant_id}", response_model=DishResponseDto, status_code=201)
def add_dish_to_menu(restaurant_id: str, dish_dto: CreateDishRequestDto, menu_service: MenuService = Depends(get_menu_service)):
    try:
        dish = menu_service.add_dish_to_menu(restaurant_id, dish_dto)
        return DishResponseDto.from_domain(dish)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
