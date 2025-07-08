from src.common.application import ApplicationException, ExceptionApplicationType

class ReservationDurationExceededException(ApplicationException):
    """
    Raised when a reservation is attempted for longer than 
    the maximum allowed duration of four hours.
    """
    def __init__(self):
        super().__init__(
            message="Cannot reserve for more than four hours.",
            app_type=ExceptionApplicationType.CONFLICT
        )
