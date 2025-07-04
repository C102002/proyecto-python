# app/schemas/restaurant.py
from typing import List
from pydantic import BaseModel, Field
from datetime import time

from src.restaurant.infraestructure.dtos.request.create_table_request_inf_dto import CreateTableRequestInfDTO

class CreateRestaurantRequestInfDTO(BaseModel):
    lat: float = Field(0.0, description="Latitud del restaurante, en grados decimales")
    lng: float = Field(0.0, description="Longitud del restaurante, en grados decimales")
    name: str = Field("Mi Restaurante", description="Nombre del restaurante")
    opening_time: time = Field(
        default_factory=lambda: time.fromisoformat("09:00:00"),
        description="Hora de apertura (HH:MM:SS)"
    )
    closing_time: time = Field(
        default_factory=lambda: time.fromisoformat("22:00:00"),
        description="Hora de cierre (HH:MM:SS)"
    )
    tables: List[CreateTableRequestInfDTO] = Field(
        default_factory=list,
        description="Listado de mesas que se crearán junto al restaurante"
    )

    class Config:
        title = "CreateRestaurantRequestDTO"
