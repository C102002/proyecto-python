from abc import ABC, abstractmethod
from typing import List

class ILogger(ABC):
    @abstractmethod
    def success_log(self, service_name: str, input: str, time: str) -> None:
        pass

    @abstractmethod
    def error_log(self, service_name: str, message: str, input: str, time: str, cause: List[str]) -> None:
        pass