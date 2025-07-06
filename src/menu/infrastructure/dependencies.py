from fastapi import Depends
from sqlalchemy.orm import Session
from src.common.infrastructure.database import get_db
from src.menu.application.services.menu_service import MenuService
from src.menu.infrastructure.repositories.menu_repository import MenuRepository

def get_menu_service(db: Session = Depends(get_db)) -> MenuService:
    menu_repository = MenuRepository(db)
    return MenuService(menu_repository, menu_repository)
