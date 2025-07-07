from pydantic import BaseModel, Field

class CreateDishRequesInftDto(BaseModel):
    name: str = Field(..., description="Dish name")
    description: str = Field(..., description="Dish description")
    price: float = Field(..., description="Dish price")
    category: str = Field(..., description="Dish category")
    image: str | None = Field(description="Dish image")

    class Config:
        extra = "forbid"