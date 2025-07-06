from typing import List
from pydantic import BaseModel, Field
from datetime import time

from src.restaurant.infraestructure.dtos.request.create_table_request_inf_dto import (
    CreateTableRequestInfDTO
)

class CreateRestaurantRequestInfDTO(BaseModel):
    lat: float = Field(
        ..., 
        description="Latitud del restaurante, en grados decimales"
    )
    lng: float = Field(
        ..., 
        description="Longitud del restaurante, en grados decimales"
    )
    name: str = Field(
        ..., 
        description="Nombre del restaurante"
    )
    opening_time: time = Field(
        ...,
        description="Hora de apertura (HH:MM:SS)"
    )
    closing_time: time = Field(
        ...,
        description="Hora de cierre (HH:MM:SS)"
    )
    tables: List[CreateTableRequestInfDTO] = Field(
        default_factory=list,
        description="Listado de mesas que se crearán junto al restaurante"
    )

    class Config:
        title = "CreateRestaurantRequestDTO"
        json_schema_extra = {
            "example": {
                "lat": -0.180653,
                "lng": -78.467834,
                "name": "Mi Restaurante",
                "opening_time": "09:00:00",
                "closing_time": "22:00:00",
                "tables": [
                    {"number": 1, "capacity": 4, "location": "terraza"},
                    {"number": 2, "capacity": 2, "location": "interior"}
                ]
            }
        }
