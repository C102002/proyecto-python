from fastapi import Depends
from sqlalchemy.orm import Session
from src.common.infrastructure.database import get_db
from src.menu.application.services.add_dish_to_menu_service import AddDishToMenuService
from src.menu.infrastructure.repositories.menu_repository import MenuRepository

def get_menu_service(db: Session = Depends(get_db)) -> AddDishToMenuService:
    menu_repository = MenuRepository(db)
    return AddDishToMenuService(menu_repository, menu_repository)
