from fastapi import Depends
from src.common.infrastructure.jwt.jwt_generator import JwtGenerator
from fastapi.security import OAuth2PasswordBearer
from ..roles.role_scopes import ALL_KNOWN_SCOPES
class JwtTransformer:

    def __init__(self):
        self.jwt_generator = JwtGenerator()

    def __call__(self, token: str = Depends(OAuth2PasswordBearer(tokenUrl="/login", scopes=ALL_KNOWN_SCOPES))):
        return self.jwt_generator.decode_token(token)