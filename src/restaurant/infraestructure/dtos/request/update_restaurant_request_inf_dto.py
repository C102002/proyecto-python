from typing import Optional
from datetime import time
from pydantic import BaseModel, Field

class UpdateRestaurantRequestInfDTO(BaseModel):
    lat: Optional[float] = Field(
        None,
        description="New latitude of the restaurant"
    )
    lng: Optional[float] = Field(
        None,
        description="New longitude of the restaurant"
    )
    name: Optional[str] = Field(
        None,
        description="New name of the restaurant"
    )
    opening_time: Optional[time] = Field(
        None,
        description="New opening time of the restaurant"
    )
    closing_time: Optional[time] = Field(
        None,
        description="New closing time of the restaurant"
    )

    class Config:
        title = "UpdateRestaurantRequestInfDTO"
        schema_extra = {
            "example": {
                "id": "87083ac1-4700-4c08-9b7c-fc3676a7ad6e",
                "lat": 10.4806,
                "lng": -66.9036,
                "name": "Nuevo Restaurante",
                "opening_time": "08:00:00",
                "closing_time": "22:00:00"
            }
        }
