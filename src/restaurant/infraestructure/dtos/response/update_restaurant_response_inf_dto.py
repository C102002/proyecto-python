from datetime import time
from pydantic import BaseModel, Field

class UpdateRestaurantResponseInfDTO(BaseModel):
    id: str = Field(
        ...,
        description="UUID of the updated restaurant"
    )
    lat: float = Field(
        ...,
        description="Latitude of the restaurant"
    )
    lng: float = Field(
        ...,
        description="Longitude of the restaurant"
    )
    name: str = Field(
        ...,
        description="Name of the restaurant"
    )
    opening_time: time = Field(
        ...,
        description="Opening time of the restaurant"
    )
    closing_time: time = Field(
        ...,
        description="Closing time of the restaurant"
    )

    class Config:
        title = "UpdateRestaurantResponseInfDTO"
        schema_extra = {
            "example": {
                "id": "87083ac1-4700-4c08-9b7c-fc3676a7ad6e",
                "lat": 10.4806,
                "lng": -66.9036,
                "name": "Mi Restaurante Actualizado",
                "opening_time": "09:00:00",
                "closing_time": "23:00:00"
            }
        }
