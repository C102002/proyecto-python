from src.auth.application.encryptor.encryptor import IEncryptor
import bcrypt

class BcryptEncryptor(IEncryptor):

    def encrypt(self, plain_data: str) -> str:
        return bcrypt.hashpw(plain_data.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def verify_password(self, plain_data: str, hashed_data: str) -> bool:
        return bcrypt.checkpw(plain_data.encode("utf-8"), hashed_data.encode("utf-8"))