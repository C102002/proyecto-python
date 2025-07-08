from src.common.application import ApplicationException, ExceptionApplicationType

class TableNotAvailableException(ApplicationException):
    """
    Raised when attempting to reserve a table that is not available.
    """
    def __init__(self):
        super().__init__(
            message="Table not available.",
            app_type=ExceptionApplicationType.CONFLICT
        )
