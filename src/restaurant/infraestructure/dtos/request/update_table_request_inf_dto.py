from typing import Optional
from pydantic import BaseModel, Field

from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum

class UpdateTableRequestInfDTO(BaseModel):
    new_number: Optional[int] = Field(
        None,
        description="Nuevo identificador de la mesa (opcional)"
    )
    capacity: Optional[int] = Field(
        None,
        description="Nueva capacidad de la mesa (opcional)"
    )
    location: Optional[TableLocationEnum] = Field(
        None,
        description="Nueva ubicación física de la mesa (opcional)"
    )

    class Config:
        title = "UpdateTableRequestInfDTO"
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "new_number": 5,
                "capacity": 6,
                "location": "terraza"
            }
        }
