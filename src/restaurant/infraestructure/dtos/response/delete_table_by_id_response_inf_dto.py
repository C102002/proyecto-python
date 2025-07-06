from pydantic import BaseModel, Field

class DeleteTableByIdResponseInfDTO(BaseModel):
    restaurant_id: str = Field(
        ...,
        description="UUID of the restaurant"
    )
    table_id: int = Field(
        ...,
        description="Identifier of the deleted table"
    )

    class Config:
        title = "DeleteTableByIdResponseInfDTO"
