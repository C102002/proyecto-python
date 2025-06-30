from abc import ABC, abstractmethod

class IEncryptor(ABC):

    @abstractmethod
    def encrypt(self, plain_data: str) -> str:
        pass
    
    @abstractmethod
    def verify_password(self, plain_data: str, hashed_data: str) -> bool:
        pass