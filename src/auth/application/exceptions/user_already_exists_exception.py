from src.common.application import ApplicationException

class UserAlreadyExistsException(ApplicationException):

    def __init__(self, email: str):
        super().__init__(f"User with email: {email}. Already exists")