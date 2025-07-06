from fastapi import FastAPI
from src.menu.infrastructure.routers.menu_router import router as menu_router

class MenuController:
    def __init__(self, app: FastAPI):
        app.include_router(menu_router, tags=["menu"])
