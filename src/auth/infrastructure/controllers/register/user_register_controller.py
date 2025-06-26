from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

class UserRegisterController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.oauth2_scheme = OAuth2PasswordBearer("/login")
        self.setup_routes()

    def setup_routes(self):
        @self.app.post("/register")
        async def register_user(token: str = Depends(self.oauth2_scheme)):
            print(token)
            return token