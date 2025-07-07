from pydantic import BaseModel
from src.menu.domain.entities.dish import Dish

class DishResponseDto(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category: str
    image: str | None = None
    is_available: bool

    @staticmethod
    def from_domain(dish: "Dish"):
        return DishResponseDto(
            id=str(dish.id.value),
            name=dish.name.value,
            description=dish.description.value,
            price=dish.price.value,
            category=dish.category.value,
            image=dish.image.value if dish.image else None,
            is_available=dish.is_available
        )
