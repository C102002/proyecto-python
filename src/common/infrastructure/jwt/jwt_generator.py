from src.common.application import ITokenGenerator
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException

load_dotenv()

class JwtGenerator(ITokenGenerator):

    def __init__(self):
        secret = os.getenv("JWT_SECRET")
        assert secret is not None, "La variable JWT_SECRET no está definida"
        self.secret = secret


    def generate_token(self, data: dict) -> str:
        data_copy = data.copy()
        expires = datetime.now(timezone.utc) + timedelta(minutes=15)

        data_copy.update({"exp": expires})

        token = jwt.encode(data_copy, self.secret, algorithm="HS256")
        return token

    
    def decode_token(self, token: str) -> str:
        try:
            token_decode = jwt.decode(token, self.secret, algorithms=["HS256"])
            user_email = token_decode.get("sub")

            if user_email is None:
                raise HTTPException(status_code=401, detail="Token inválido", headers={"WWW-Authenticate": "Bearer"})
            
            return user_email
        except JWTError:
            raise HTTPException(status_code=401, detail="Token inválido", headers={"WWW-Authenticate": "Bearer"})