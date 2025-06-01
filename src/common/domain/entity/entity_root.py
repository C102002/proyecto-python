from typing import Generic, TypeVar
from ..value_object.value_object_root import ValueObjectRoot

T = TypeVar('T', bound=ValueObjectRoot)

class EntityRoot(Generic[T]):
    def __init__(self, id: T):
        self._id = id

    @property
    def id(self) -> T:
        return self._id