from src.common.domain import DomainException

class InvalidRestaurantException(DomainException):

    def __init__(self):
        super().__init__("Invalid Restaurant")