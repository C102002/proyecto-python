from fastapi import FastAPI, Depends
from src.common.infrastructure import JwtTransformer

class UserRegisterController:
    def __init__(self, app: FastAPI):
        self.app = app

        self.setup_routes()

    async def init(self):
        pass

    def setup_routes(self):
        @self.app.post("/register")
        async def register_user(token: str = Depends(JwtTransformer())):
            print(token)
            return token