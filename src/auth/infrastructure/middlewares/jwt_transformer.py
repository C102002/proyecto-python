from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.common.infrastructure import ALL_KNOWN_SCOPES, JwtGenerator
class JwtTransformer:

    def __init__(self):
        self.jwt_generator = JwtGenerator()

    def __call__(self, token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/login", scopes=ALL_KNOWN_SCOPES))):
        return self.jwt_generator.decode_token(token)