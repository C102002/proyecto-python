from src.common.domain import DomainException

class InvalidRestaurantNameException(DomainException):

    def __init__(self, name: str):
        super().__init__(f"Invalid Restaurant name: {name}, Name must exist and have at least 3 characteres")