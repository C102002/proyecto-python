from src.common.domain import DomainException

class InvalidClosingTimeException(DomainException):
    
    def __init__(self, closing_time: str):
        super().__init__(f"Invalid Closing Time: {closing_time}, format espected HH:MM o HH:MM:SS")