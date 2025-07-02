from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.application.services.user_login_service import UserLoginService
from src.common.infrastructure import PostgresDatabase
from src.auth.infrastructure.repositories.query.orm_user_query_repository import OrmUserQueryRepository
from src.auth.infrastructure.encryptor.bcrypt_encryptor import BcryptEncryptor
from src.common.infrastructure import JwtGenerator
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.auth.application.dtos.request.user_login_request_dto import UserLoginRequestDto

class UserLoginController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.user_login_service = None
        self.setup_routes()

    async def init(self):
        session_generator = PostgresDatabase().get_session()
        session = await anext(session_generator)
        user_query_repository = OrmUserQueryRepository(session)
        encryptor = BcryptEncryptor()
        jwt_generator = JwtGenerator()

        self.user_login_service = UserLoginService(
            user_query_repository=user_query_repository,
            encryptor=encryptor,
            token_generator=jwt_generator
        )

    def setup_routes(self):
        @self.app.post("/login")
        async def login(form_data: OAuth2PasswordRequestForm = Depends()):
            if self.user_login_service is None:
                raise RuntimeError("UserLoginService not initialized. Did you forget to call init()?")

            service = ExceptionDecorator(self.user_login_service)

            response = await service.execute(UserLoginRequestDto(
                email=form_data.username,
                password=form_data.password
            ))
            return {
                "access_token": response.value.token,
                "token_type": "bearer"
            }