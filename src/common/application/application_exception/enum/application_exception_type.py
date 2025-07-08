from enum import Enum

class ExceptionApplicationType(Enum):
    CONFLICT = "CONFLICT",
    FORBIDDEN = "FORBIDDEN",
    NOT_FOUND = "NOT_FOUND",
    APPLICATION_ERROR = "APPLICATION_ERROR"
