from pydantic import BaseModel, Field

class DeleteRestaurantByIdRequestInfDTO(BaseModel):
    restaurant_id: str = Field(
        ...,
        description="UUID unique of the restaurant"
    )

    class Config:
        title = "DeleteRestaurantByIdResponseInfDTO"
