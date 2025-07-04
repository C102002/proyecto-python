from src.common.application import ApplicationException, ExceptionApplicationType

class UserAlreadyExistsException(ApplicationException):

    def __init__(self, email: str):
        super().__init__(f"User with email: {email}. Already exists", ExceptionApplicationType.CONFLICT)