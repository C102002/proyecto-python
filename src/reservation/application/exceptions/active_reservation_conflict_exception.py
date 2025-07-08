from src.common.application import ApplicationException, ExceptionApplicationType

class ActiveReservationConflictException(ApplicationException):
    """
    Raised when a client already has an active reservation
    in the same time slot.
    """
    def __init__(self):
        super().__init__(
            message="Client already has an active reservation at the same time.",
            app_type=ExceptionApplicationType.CONFLICT
        )
