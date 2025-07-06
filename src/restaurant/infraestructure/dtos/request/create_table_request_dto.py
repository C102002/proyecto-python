from pydantic import BaseModel, Field
from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum

class CreateTableRequestInfDTO(BaseModel):
    restaurant_id: str = Field(
        ...,
        description="UUID of the restaurant this table belongs to"
    )
    number: int = Field(
        ...,
        description="Table identifier number"
    )
    capacity: int = Field(
        ...,
        description="Maximum number of diners the table can seat"
    )
    location: TableLocationEnum = Field(
        ...,
        description="Physical location of the table"
    )

    class Config:
        title = "CreateTableRequestInfDTO"
        use_enum_values = True
