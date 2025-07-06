from pydantic import BaseModel, Field

class DeleteRestaurantByIdResponseInfDTO(BaseModel):
    restaurant_id: str = Field(
        ...,
        description="UUID unique of the restaurant"
    )

    class Config:
        title = "DeleteRestaurantByIdResponseInfDTO"
