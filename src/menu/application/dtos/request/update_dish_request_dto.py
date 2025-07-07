from pydantic import BaseModel

class UpdateDishRequestDto(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    category: str | None = None
    image: str | None = None
