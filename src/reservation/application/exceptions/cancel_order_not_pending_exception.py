from src.common.application import ApplicationException, ExceptionApplicationType

class CancelOrderNotPendingException(ApplicationException):
    """
    Raised when a cancellation is attempted on an order
    that is not in the 'pending' status.
    """
    def __init__(self):
        super().__init__(
            message=(
                "Invalid cancellation: you can only cancel orders "
                "that are in pending status."
            ),
            app_type=ExceptionApplicationType.FORBIDDEN
        )
