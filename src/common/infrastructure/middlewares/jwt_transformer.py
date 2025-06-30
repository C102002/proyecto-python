from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.common.infrastructure.jwt.jwt_generator import JwtGenerator

class JwtTransformer:

    def __init__(self):
        self.jwt_generator = JwtGenerator()

    def __call__(self, token: str = Depends(OAuth2PasswordBearer(tokenUrl="/login"))):
        return self.jwt_generator.decode_token(token)