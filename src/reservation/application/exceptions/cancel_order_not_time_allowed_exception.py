from src.common.application import ApplicationException, ExceptionApplicationType

class CancelOrderTooLateException(ApplicationException):
    """
    Raised when a cancellation is attempted less than one hour
    before the scheduled order time.
    """
    def __init__(self):
        super().__init__(
            message=(
                "Invalid cancellation: you cannot cancel an order "
                "less than one hour before its scheduled time."
            ),
            app_type=ExceptionApplicationType.FORBIDDEN
        )
