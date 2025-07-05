
class GetRestaurantByIdRequestDTO:
    def __init__(self, restaurant_id: str):
        """
        DTO para solicitar un restaurante por su UUID.

        :param restaurant_id: UUID único del restaurante
        """
        self.restaurant_id: str = restaurant_id

    def __repr__(self):
        return (
            f"GetRestaurantByIdRequestInfDTO("
            f"restaurant_id={self.restaurant_id!r}"
            f")"
        )
