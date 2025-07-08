from src.common.application import ApplicationException, ExceptionApplicationType

class RestaurantNotFoundException(ApplicationException):
    """
    Raised when attempting to reference a restaurant that does not exist.
    """
    def __init__(self):
        super().__init__(
            message="Restaurant not found.",
            app_type=ExceptionApplicationType.NOT_FOUND
        )
