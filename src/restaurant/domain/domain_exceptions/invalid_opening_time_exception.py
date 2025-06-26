from src.common.domain import DomainException

class InvalidOpeningTimeException(DomainException):
    
    def __init__(self, opening_time: str):
        super().__init__(f"Invalid Opening Time: {opening_time}, format espected HH:MM o HH:MM:SS")