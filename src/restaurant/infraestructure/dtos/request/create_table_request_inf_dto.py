# app/schemas/table.py
from pydantic import BaseModel, Field
from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum

class CreateTableRequestInfDTO(BaseModel):
    number: int = Field(
        1,
        ge=1,
        description="Número identificador de la mesa dentro del restaurante"
    )
    capacity: int = Field(
        4,
        ge=1,
        description="Cantidad máxima de comensales que puede sentar la mesa"
    )
    location: TableLocationEnum = Field(
        default_factory=lambda: TableLocationEnum.terraza,
        description="Ubicación física de la mesa (terraza, interior, parque, jardín interno, jardín externo)"
    )

    class Config:
        title = "CreateTableRequestInfDTO"
        use_enum_values = True
