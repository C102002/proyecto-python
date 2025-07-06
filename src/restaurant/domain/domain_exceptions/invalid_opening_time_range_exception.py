from src.common.domain import DomainException

class InvalidOpeningTimeRangeException(DomainException):
    
    def __init__(self, opening_time: str):
        super().__init__(f"Invalid Opening Time: {opening_time}, Valid Range between 00:00:00 and 23:59:59.999999")