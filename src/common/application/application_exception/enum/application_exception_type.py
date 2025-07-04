from enum import Enum

class ExceptionApplicationType(Enum):
    CONFLICT = "CONFLICT"
    FORBIDDEN = "FORBIDDEN"
    APPLICATION_ERROR = "APPLICATION_ERROR"
