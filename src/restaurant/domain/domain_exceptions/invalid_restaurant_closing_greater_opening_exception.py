from src.common.domain import DomainException

class InvalidRestaurantClosingGreaterOpeningException(DomainException):

    def __init__(self, opening_time:str,closing_time:str):
        super().__init__(f"Invalid Restaurant the opening time {opening_time} is bigger than the closing time {closing_time}")