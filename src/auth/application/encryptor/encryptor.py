from abc import ABC, abstractmethod

class IEncryptor(ABC):

    @abstractmethod
    def encrypt(self, plane_data: str) -> str:
        pass
    
    @abstractmethod
    def decrypt(self, hashed_data: str) -> str:
        pass