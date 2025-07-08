class CreateDishRequestDto:
    
    def __init__(
            self,
            name: str,
            restaurant_id: str,
            description: str,
            price: float,
            category: str,
            image: str | None = None
            ) -> None:
        self.name = name
        self.restaurant_id = restaurant_id
        self.description = description
        self.price = price
        self.category = category
        self.image = image
