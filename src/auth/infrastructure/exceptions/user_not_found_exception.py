from src.common.infrastructure import InfrastructureException, ExceptionInfrastructureType

class UserNotFoundException(InfrastructureException):

    def __init__(self, ):
        super().__init__("User not found", ExceptionInfrastructureType.USER_NOT_FOUND)