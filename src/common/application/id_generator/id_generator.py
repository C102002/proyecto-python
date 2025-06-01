from abc import ABC, abstractmethod

class IIdGenerator(ABC):

    @abstractmethod
    def generate_id(self) -> str:
        pass