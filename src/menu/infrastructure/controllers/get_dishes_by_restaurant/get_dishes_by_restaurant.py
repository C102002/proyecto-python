from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.menu.application.dtos.response.dish_response_dto import DishResponseDto
from src.menu.application.services.menu_service import MenuService
from src.menu.infrastructure.dependencies import get_menu_service

router = APIRouter()

@router.get("/dishes/{restaurant_id}", response_model=List[DishResponseDto])
def get_dishes_by_restaurant(restaurant_id: str, menu_service: MenuService = Depends(get_menu_service)):
    try:
        menu = menu_service.get_menu_by_restaurant_id(restaurant_id)
        if not menu:
            return []
        return [DishResponseDto.from_domain(dish) for dish in menu.dishes]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
