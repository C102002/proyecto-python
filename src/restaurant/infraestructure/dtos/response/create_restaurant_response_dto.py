from pydantic import BaseModel, Field
from datetime import time


class CreateRestaurantResponseDTO(BaseModel):
    id: str = Field(..., description="UUID único del restaurante")
    lat: float = Field(..., description="Latitud del restaurante en grados decimales")
    lng: float = Field(..., description="Longitud del restaurante en grados decimales")
    name: str = Field(..., description="Nombre del restaurante")
    opening_time: time = Field(..., description="Hora de apertura (formato HH:MM:SS)")
    closing_time: time = Field(..., description="Hora de cierre (formato HH:MM:SS)")

    class Config:
        title = "CreateRestaurantResponseDTO"
