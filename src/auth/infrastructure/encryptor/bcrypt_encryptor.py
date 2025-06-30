from passlib.context import CryptContext
from src.auth.application.encryptor.encryptor import IEncryptor

class BcryptEncryptor(IEncryptor):
    def __init__(self):
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def encrypt(self, plain_data: str) -> str:
        return self.context.hash(plain_data)

    def verify_password(self, plain_data: str, hashed_data: str) -> bool:
        return self.context.verify(plain_data, hashed_data)
