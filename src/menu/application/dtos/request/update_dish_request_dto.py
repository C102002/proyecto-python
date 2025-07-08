class UpdateDishRequestDto:
    
    def __init__(
            self,
            name: str | None,
            description: str | None,
            price: float | None,
            category: str | None,
            image: str | None,
            dish_id: str
            ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image = image
        self.dish_id = dish_id
