from src.common.application import ITokenGenerator
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException
from src.auth.domain.enum.user_role_enum import UserRoleEnum
from ..roles.role_scopes import ROLE_SCOPES

load_dotenv()

class JwtGenerator(ITokenGenerator):

    def __init__(self):
        secret = os.getenv("JWT_SECRET")
        assert secret is not None, "La variable JWT_SECRET no está definida"
        self.secret = secret

    def generate_token(self, data: dict, role: UserRoleEnum) -> str:
        data_copy = data.copy()
        expires = datetime.now(timezone.utc) + timedelta(minutes=15)

        data_copy.update({"exp": expires})

        roles = ROLE_SCOPES.get(UserRoleEnum.CLIENT, [])

        if (role == UserRoleEnum.ADMIN):
            roles = ROLE_SCOPES.get(UserRoleEnum.ADMIN, []) 
        
        data_copy.update({"scopes": roles})

        token = jwt.encode(data_copy, self.secret, algorithm="HS256")
        return token

    
    def decode_token(self, token: str) -> dict:
        try:
            token_decode = jwt.decode(token, self.secret, algorithms=["HS256"])

            if token_decode["sub"] is None or token_decode["scopes"] is None:
                raise HTTPException(status_code=401, detail="Unauthorized: Invalid token.", headers={"WWW-Authenticate": "Bearer"})

            return token_decode
        except JWTError:
            raise HTTPException(status_code=401, detail="Unauthorized: Invalid token.", headers={"WWW-Authenticate": "Bearer"})