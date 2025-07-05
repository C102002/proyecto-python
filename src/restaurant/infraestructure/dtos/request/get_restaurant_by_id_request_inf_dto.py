from pydantic import BaseModel, Field

class GetRestaurantByIdRequestInfDTO(BaseModel):
    page: str = Field(
        ...,
        description="UUID único del restaurante"
        )

    class Config:
        title = "GetRestaurantByIdRequestInfDTO"
