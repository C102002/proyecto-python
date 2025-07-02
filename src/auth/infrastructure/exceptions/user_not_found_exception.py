from src.common.infrastructure import InfrastructureException

class UserNotFoundException(InfrastructureException):

    def __init__(self, ):
        super().__init__("User not found")