from pydantic import BaseModel

class CreateDishRequestDto(BaseModel):
    name: str
    description: str
    price: float
    category: str
    image: str | None = None
