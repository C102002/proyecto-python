from src.common.application import ApplicationException, ExceptionApplicationType

class InvalidCredentialsException(ApplicationException):

    def __init__(self):
        super().__init__("Invalid credentials provided. Please check your email and password", ExceptionApplicationType.FORBIDDEN)
