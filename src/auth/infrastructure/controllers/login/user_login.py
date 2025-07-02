from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.application.services.user_login_service import UserLoginService
from src.common.infrastructure import PostgresDatabase
from src.auth.infrastructure.repositories.query.orm_user_query_repository import OrmUserQueryRepository
from src.auth.infrastructure.encryptor.bcrypt_encryptor import BcryptEncryptor
from src.common.infrastructure import JwtGenerator, GetPostgresqlSession
from src.common.application.aspects.exception_decorator.exception_decorator import ExceptionDecorator
from src.auth.application.dtos.request.user_login_request_dto import UserLoginRequestDto
from sqlalchemy.ext.asyncio import AsyncSession

class UserLoginController:
    def __init__(self, app: FastAPI):
        self.app = app

        self.setup_routes()

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        user_query_repository = OrmUserQueryRepository(postgres_session)
        encryptor = BcryptEncryptor()
        jwt_generator = JwtGenerator()

        user_login_service = UserLoginService(
            user_query_repository=user_query_repository,
            encryptor=encryptor,
            token_generator=jwt_generator
        )

        return user_login_service

    def setup_routes(self):
        @self.app.post("/login")
        async def login(form_data: OAuth2PasswordRequestForm = Depends(), login_service: UserLoginService = Depends(self.get_service)):
            if login_service is None:
                raise RuntimeError("UserLoginService not initialized. Did you forget to call init()?")

            service = ExceptionDecorator(login_service)

            response = await service.execute(UserLoginRequestDto(
                email=form_data.username,
                password=form_data.password
            ))
            return {
                "access_token": response.value.token,
                "token_type": "bearer"
            }