from src.common.domain import DomainException

class InvalidLocationLongitudeException(DomainException):

    def __init__(self, longitude: float):
        super().__init__(
            f"Invalid restaurant location longitude: {longitude}. Must be between -180.0 and 180.0."
        )
