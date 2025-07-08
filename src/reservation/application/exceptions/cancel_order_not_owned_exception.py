from src.common.application import ApplicationException, ExceptionApplicationType

class CancelOrderNotOwnedExeption(ApplicationException):

    def __init__(self):
        super().__init__(message=f"Invalid id provided. You cant cancell an order that is not yours, please cancel your own orders", app_type=ExceptionApplicationType.FORBIDDEN)
