from typing import List
from pydantic import BaseModel, Field
from datetime import time

from src.restaurant.infraestructure.dtos.response.create_table_response_inf_dto import CreateTableResponseInfDTO


class GetRestaurantByIdResponseInfDTO(BaseModel):
    id: str = Field(..., description="UUID único del restaurante")
    lat: float = Field(..., description="Latitud del restaurante en grados decimales")
    lng: float = Field(..., description="Longitud del restaurante en grados decimales")
    name: str = Field(..., description="Nombre del restaurante")
    opening_time: time = Field(..., description="Hora de apertura (formato HH:MM:SS)")
    closing_time: time = Field(..., description="Hora de cierre (formato HH:MM:SS)")
    tables: List[CreateTableResponseInfDTO] = Field(
        default_factory=list,
        description="Listado de mesas que son del restaurante"
    )
    class Config:
        title = "GetRestaurantByIdResponseInfDTO"
