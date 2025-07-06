class DeleteTableByIdResponseDTO:
    def __init__(self, restaurant_id: str, table_id: int):
        """
        DTO for deleting a table by its ID within a restaurant.

        :param restaurant_id: UUID of the restaurant
        :param table_id:  Identifier of the table to delete
        """
        self.restaurant_id: str = restaurant_id
        self.table_id: int = table_id

    def __repr__(self):
        return (
            f"DeleteTableByIdResponseDTO("
            f"restaurant_id={self.restaurant_id!r}, "
            f"table_id={self.table_id!r}"
            f")"
        )
