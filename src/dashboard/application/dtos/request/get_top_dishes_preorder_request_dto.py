from typing import Optional

class GetTopDishesPreorderRequestDTO:
    """
    DTO to obtain the most preordered dishes
    """

    def __init__(self, top_n: Optional[int] = 5):
        self.top_n = top_n

    def __repr__(self):
        return f"DishPreorderRequestDTO(top_n={self.top_n!r})"
