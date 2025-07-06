class GetRestaurantByIdRequestDTO:
    def __init__(self, restaurant_id: str):
        """
        DTO for requesting a restaurant by its UUID.

        :param restaurant_id: Unique UUID of the restaurant
        """
        self.restaurant_id: str = restaurant_id

    def __repr__(self):
        return (
            f"GetRestaurantByIdRequestDTO("
            f"restaurant_id={self.restaurant_id!r}"
            f")"
        )
