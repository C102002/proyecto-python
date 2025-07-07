from pydantic import BaseModel, Field

class UpdateTableResponseInfDTO(BaseModel):
    number: int = Field(
        ...,
        description="Identifier of the updated table"
    )
    capacity: int = Field(
        ...,
        description="Updated seating capacity of the table"
    )
    location: str = Field(
        ...,
        description="Updated physical location of the table"
    )
    restaurant_id: str = Field(
        ...,
        description="UUID of the restaurant this table belongs to"
    )

    class Config:
        title = "UpdateTableResponseInfDTO"
        json_schema_extra = {
            "example": {
                "number": "1",
                "capacity": 4,
                "location": "terraza",
                "restaurant_id": "87083ac1-4700-4c08-9b7c-fc3676a7ad6e"
            }
        }
