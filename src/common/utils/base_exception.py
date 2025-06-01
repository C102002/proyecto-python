from .base_exception_enum import BaseExceptionEnum

class BaseException(Exception):

    def __init__(self, message: str, exception_type: BaseExceptionEnum = BaseExceptionEnum.NOT_REGISTERED):
        super().__init__(message)
        self._type = exception_type
        self._stacks: list[str] = []

    def add_exceptions(self, *exceptions: str) -> None:
        self._stacks.extend(exceptions)

    @property
    def type(self) -> BaseExceptionEnum:
        return self._type

    @property
    def stacks(self) -> list[str]:
        return self._stacks.copy()