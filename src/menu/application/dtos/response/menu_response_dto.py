from pydantic import BaseModel
from typing import List
from src.menu.application.dtos.response.dish_response_dto import DishResponseDto
from src.menu.domain.aggregate.menu import Menu

class MenuResponseDto(BaseModel):
    id: str
    restaurant_id: str
    dishes: List[DishResponseDto]
    categories: List[str]

    @staticmethod
    def from_domain(menu: "Menu"):
        return MenuResponseDto(
            id=str(menu.id.value),
            restaurant_id=str(menu.restaurant_id.value),
            dishes=[DishResponseDto.from_domain(dish) for dish in menu.dishes],
            categories=menu.categories
        )
