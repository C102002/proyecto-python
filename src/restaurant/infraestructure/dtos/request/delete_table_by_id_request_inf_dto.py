from pydantic import BaseModel, Field

class DeleteTableByIdRequestInfDTO(BaseModel):
    restaurant_id: str = Field(
        ...,
        description="UUID of the restaurant"
    )
    table_id: int = Field(
        ...,
        description="Identifier of the table to delete"
    )

    class Config:
        title = "DeleteTableByIdRequestInfDTO"
