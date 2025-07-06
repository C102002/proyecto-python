from src.common.domain import DomainException

class InvalidClosingTimeRangeException(DomainException):
    
    def __init__(self, closing_time: str):
        super().__init__(f"Invalid Closing Time: {closing_time}, Valid Range between 00:00:00 and 23:59:59.999999")