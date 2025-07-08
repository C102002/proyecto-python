from pydantic import BaseModel, Field

class UpdateDishRequestInfDto(BaseModel):
    name: str | None = Field(description="Dish name", default=None)
    description: str | None = Field(description="Dish description", default=None)
    price: float | None = Field(description="Dish price", default=None)
    category: str | None = Field(description="Dish category", default=None)
    image: str | None = Field(description="Dish image", default=None)

    class Config:
        extra = "forbid"
