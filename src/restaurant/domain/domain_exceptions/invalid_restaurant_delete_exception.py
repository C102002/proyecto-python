from src.common.domain import DomainException

class InvalidRestaurantDeleteException(DomainException):

    def __init__(self, quantity: int):
        super().__init__(f"Invalid Restaurant delete: total tables {quantity}, the quantity of tables must be 0 but is {quantity}")