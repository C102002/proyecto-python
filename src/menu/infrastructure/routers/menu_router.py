from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.menu.application.dtos.request.create_dish_request_dto import CreateDishRequestDto
from src.menu.application.dtos.request.update_dish_request_dto import UpdateDishRequestDto
from src.menu.application.dtos.response.dish_response_dto import DishResponseDto
from src.menu.application.dtos.response.menu_response_dto import MenuResponseDto
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

@router.put("/dishes/{dish_id}", response_model=DishResponseDto)
def update_dish_in_menu(dish_id: str, dish_dto: UpdateDishRequestDto, menu_service: MenuService = Depends(get_menu_service)):
    try:
        dish = menu_service.update_dish_in_menu(dish_id, dish_dto)
        return DishResponseDto.from_domain(dish)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/dishes/{dish_id}", status_code=204)
def remove_dish_from_menu(dish_id: str, menu_service: MenuService = Depends(get_menu_service)):
    try:
        menu_service.remove_dish_from_menu(dish_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/dishes/{restaurant_id}", response_model=MenuResponseDto)
def get_menu(restaurant_id: str, menu_service: MenuService = Depends(get_menu_service)):
    try:
        menu = menu_service.get_menu_by_restaurant_id(restaurant_id)
        if not menu:
            raise HTTPException(status_code=404, detail="Menu not found")
        return MenuResponseDto.from_domain(menu)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
