from src.common.application import ApplicationException, ExceptionApplicationType

class PreorderLimitExceededException(ApplicationException):
    """
    Raised when a client tries to pre-order more than 5 dishes.
    """
    def __init__(self):
        super().__init__(
            message="Error Creating Reservation: Cannot pre-order more than 5 dishes.",
            app_type=ExceptionApplicationType.CONFLICT
        )
