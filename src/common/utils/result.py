from typing import Generic, TypeVar, Optional
from .base_exception import BaseException
from .exceptions.not_registered_exception import NotRegisteredException

T = TypeVar('T')

class Result(Generic[T]):
    def __init__(self, value: Optional[T] = None, error: Optional[BaseException] = None):
        self._value = value
        self._error = error
        
    def __repr__(self):
        return (
            f"<Result("
            f"success={self.is_success}, "
            f"value={self._value!r}, "
            f"error={self._error!r}"
            f")>"
        )

    # Opcional: __str__ igual a repr para que print(...) también lo use
    __str__ = __repr__

    @property
    def is_error(self) -> bool:
        return self._error is not None

    @property
    def is_success(self) -> bool:
        return self._value is not None

    @property
    def value(self) -> T:
        if self._value is None:
            raise NotRegisteredException("No existe un value")
        return self._value

    @property
    def error(self) -> BaseException:
        if self._error is None:
            raise NotRegisteredException("No existe ningun error")
        return self._error

    @classmethod
    def success(cls, value: T) -> 'Result[T]':
        return cls(value=value)

    @classmethod
    def fail(cls, error: BaseException) -> 'Result[T]':
        return cls(error=error)