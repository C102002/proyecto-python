# app/controllers/create_restaurant_controller.py
from typing import List
from fastapi import FastAPI
from fastapi import status

from src.restaurant.infraestructure.dtos.response.get_all_restaurant_response_dto import GetAllRestaurantResponseDTO
from ...routers.restaurant_router import restaurant_router

class GetAllRestaurantController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)

    def setup_routes(self):
        @restaurant_router.get(
            "/",
            response_model=List[GetAllRestaurantResponseDTO],
            status_code=status.HTTP_200_OK,
            summary="Conseguir todos los restaurantes",
            response_description="Datos del restaurante recién creado"
        )
        async def get_all_restaurant():
            return []
