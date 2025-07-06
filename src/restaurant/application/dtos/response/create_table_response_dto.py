
class CreateTableResponseDTO:
    def __init__(
        self,
        id: str,
        capacity: int,
        location: str,
        restaurant_id:str
    ):
        self.id = id
        self.capacity = capacity
        self.location = location
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return (
            f"TableResponseDTO(id={self.id!r}, "
            f"capacity={self.capacity!r}, "
            f"location={self.location!r},"
            f"restaurant_id={self.restaurant_id!r})"
        )