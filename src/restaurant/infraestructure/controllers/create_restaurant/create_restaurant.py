# app/controllers/create_restaurant_controller.py
from fastapi import FastAPI
from fastapi import status
from ...routers.restaurant_router import restaurant_router
from ...dtos.request.create_restaurant_request_dto import CreateRestaurantRequestDTO

class CreateRestaurantController:
    def __init__(self, app: FastAPI):
        self.setup_routes()
        app.include_router(restaurant_router)

    def setup_routes(self):
        @restaurant_router.post(
            "/",
            response_model=CreateRestaurantRequestDTO,
            status_code=status.HTTP_201_CREATED,
            summary="Crear restaurante",
            description=(
                "Crea un nuevo restaurante con:\n"
                "- latitud\n"
                "- longitud\n"
                "- nombre\n"
                "- hora de apertura\n"
                "- hora de cierre"
            ),
            response_description="Datos del restaurante recién creado"
        )
        async def create_restaurant(input_dto: CreateRestaurantRequestDTO):
            return input_dto
