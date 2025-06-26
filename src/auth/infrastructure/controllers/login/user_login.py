from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

class UserLoginController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        @self.app.post("/login")
        async def login(form_data: OAuth2PasswordRequestForm = Depends()):
            return {
                "access_token": form_data.username,
                "token_type": "bearer"
            }