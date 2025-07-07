from pydantic import BaseModel, Field

class UpdateDishRequestInfDto(BaseModel):
    name: str | None = Field(description="Dish name")
    description: str | None = Field(description="Dish description")
    price: float | None = Field(description="Dish price")
    category: str | None = Field(description="Dish category")
    image: str | None = Field(description="Dish image")

    class Config:
        extra = "forbid"
