class GetTopDishesPreorderRequestDTO:
    """
    DTO to retrieve the most pre-ordered dishes.
    """

    def __init__(self, dish_id: str, dish_name: str, total_preorders: int):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.total_preorders = total_preorders

    def __repr__(self):
        return (
            f"GetTopDishesPreorderRequestDTO("
            f"dish_id={self.dish_id!r}, "
            f"dish_name={self.dish_name!r}, "
            f"total_preorders={self.total_preorders!r}"
            f")"
        )
