from abc import ABC, abstractmethod

class ITimer(ABC):
    @abstractmethod
    def get_time(self, time1: float, time2: float) -> float:
        pass

    @abstractmethod
    def set_time(self) -> float:
        pass