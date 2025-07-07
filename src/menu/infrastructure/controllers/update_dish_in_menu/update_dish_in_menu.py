from fastapi import APIRouter, Depends, HTTPException
from src.menu.application.dtos.request.update_dish_request_dto import UpdateDishRequestDto
from src.menu.application.dtos.response.dish_response_dto import DishResponseDto
from src.menu.application.services.menu_service import MenuService
from src.menu.infrastructure.dependencies import get_menu_service

router = APIRouter()

@router.put("/dishes/{dish_id}", response_model=DishResponseDto)
def update_dish_in_menu(dish_id: str, dish_dto: UpdateDishRequestDto, menu_service: MenuService = Depends(get_menu_service)):
    try:
        dish = menu_service.update_dish_in_menu(dish_id, dish_dto)
        return DishResponseDto.from_domain(dish)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
