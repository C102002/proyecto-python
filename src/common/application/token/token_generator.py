from abc import ABC, abstractmethod

class ITokenGenerator(ABC):

    @abstractmethod
    def generate_token(self, data: dict) -> str:
        pass

    @abstractmethod
    def decode_token(self, token: str) -> str:
        pass