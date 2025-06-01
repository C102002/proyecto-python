from datetime import datetime

class CustomError(Exception):
    def __init__(self, message: str, error: str, status_code: int):
        super().__init__(message)
        self._message = message
        self._error = error
        self._status_code = status_code
        self._date = datetime.now()

    @property
    def message(self) -> str:
        return self._message

    @property
    def error(self) -> str:
        return self._error

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def date(self) -> datetime:
        return self._date
    
