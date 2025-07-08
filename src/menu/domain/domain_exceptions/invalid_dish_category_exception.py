from src.common.domain import DomainException

class InvalidDishCategoryException(DomainException):
    def __init__(self, category: str):
        super().__init__(f"Invalid dish category: {category}. Supported categories are: Main, Dessert, Appetizer")
