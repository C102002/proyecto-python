from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
from ..value_object.value_object_root import ValueObjectRoot
from ..entity.entity_root import EntityRoot
from ..domain_event.domain_event_root import DomainEventRoot

T = TypeVar('T', bound=ValueObjectRoot)

class AggregateRoot(EntityRoot[T], ABC, Generic[T]):
    def __init__(self, id: T):
        super().__init__(id)
        self._events: List[DomainEventRoot] = []

    @abstractmethod
    def when(self, event: DomainEventRoot) -> None:
        pass

    @abstractmethod
    def validate_state(self) -> None:
        pass

    def apply(self, event: DomainEventRoot) -> None:
        self.when(event)
        self.validate_state()
        self._events.append(event)

    def pull_domain_events(self) -> List[DomainEventRoot]:
        events = self._events[:]
        self._events.clear()
        return events