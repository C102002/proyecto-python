from fastapi import FastAPI, Depends, status
from src.common.infrastructure import GetPostgresqlSession
from ...middlewares.user_role_verify import UserRoleVerify
from src.auth.infrastructure.repositories.query.orm_user_query_repository import OrmUserQueryRepository
from src.auth.infrastructure.repositories.command.orm_user_command_repository import OrmUserCommandRepository
from src.auth.infrastructure.encryptor.bcrypt_encryptor import BcryptEncryptor
from src.auth.application.services.user_register_service import UserRegisterService
from src.common.infrastructure import UuidGenerator
from ...dtos.request.user_register_request_inf_dto import UserRegisterRequestInfDto
from src.auth.application.dtos.request.user_register_request_dto import UserRegisterRequestDto
from src.common.application import ExceptionDecorator
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from ...routers.auth_router import auth_router

class UserRegisterController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()
        app.include_router(auth_router)

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        encryptor = BcryptEncryptor()
        id_generator = UuidGenerator()
        orm_user_query_repository = OrmUserQueryRepository(postgres_session)
        orm_user_command_repository = OrmUserCommandRepository(postgres_session)

        user_register_service = UserRegisterService(
            orm_user_query_repository,
            orm_user_command_repository,
            encryptor,
            id_generator
        )

        return user_register_service

    def setup_routes(self):
        @auth_router.post(
            "/register",
            response_model=None,
            status_code=status.HTTP_201_CREATED,
            summary="Register a user",
            description=(
                "Crea un nuevo usuario con:\n"
                "- nombre\n"
                "- email\n"
                "- password\n"
            ),
            response_description="No devuelve ningun valor"
        )
        async def register_user(user: UserRegisterRequestInfDto, register_service: UserRegisterService = Depends(self.get_service)):

            if register_service is None:
                raise RuntimeError("UserRegisterService not initialized. Did you forget to call init()?")

            service = ExceptionDecorator(register_service, FastApiErrorHandler())

            request = UserRegisterRequestDto(
                email=user.email,
                name=user.name,
                password=user.password,
            )

            response = await service.execute(request)

            return None