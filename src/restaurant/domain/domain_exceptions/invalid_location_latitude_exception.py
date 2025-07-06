from src.common.domain import DomainException

class InvalidLocationLatitudeException(DomainException):

    def __init__(self, latitude: float):
        super().__init__(
            f"Invalid restaurant location latitude: {latitude}. Must be between -90.0 and 90.0."
        )
