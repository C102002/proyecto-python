from src.common.utils.base_exception import BaseException

class InvalidDishCategoryException(BaseException):
    def __init__(self, category: str):
        super().__init__(f"Invalid dish category: {category}. Supported categories are: Main, Dessert, Appetizer")
