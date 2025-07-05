from fastapi import APIRouter, Depends, HTTPException
from src.menu.application.services.menu_service import MenuService
from src.menu.infrastructure.dependencies import get_menu_service

router = APIRouter()

@router.delete("/dishes/{dish_id}", status_code=204)
def remove_dish_from_menu(dish_id: str, menu_service: MenuService = Depends(get_menu_service)):
    try:
        menu_service.remove_dish_from_menu(dish_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
