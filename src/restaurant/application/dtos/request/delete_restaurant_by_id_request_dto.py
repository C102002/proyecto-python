
class DeleteRestaurantByIdRequestDTO:
    def __init__(self, restaurant_id: str):
        """
        DTO to delete a restaurant by UUID.

        :param restaurant_id: UUID is unique of the restaurant
        """
        self.restaurant_id: str = restaurant_id

    def __repr__(self):
        return (
            f"DeleteRestaurantByIdRequestDTO("
            f"restaurant_id={self.restaurant_id!r}"
            f")"
        )
