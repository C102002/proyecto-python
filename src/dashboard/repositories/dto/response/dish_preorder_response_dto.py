from typing import NamedTuple


class DishPreorderResponseDTO(NamedTuple):
    """
    Platos más pre-ordenados.
    """
    dish_id: str
    dish_name: str
    total_preorders: int


