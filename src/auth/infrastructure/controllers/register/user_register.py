from fastapi import FastAPI, Security
from src.common.infrastructure import PostgresDatabase, UserRoleVerify
from src.auth.infrastructure.repositories.query.orm_user_query_repository import OrmUserQueryRepository
from src.auth.infrastructure.repositories.command.orm_user_command_repository import OrmUserCommandRepository
from src.auth.infrastructure.encryptor.bcrypt_encryptor import BcryptEncryptor
from src.auth.application.services.user_register_service import UserRegisterService
from src.common.infrastructure import UuidGenerator
from ...dtos.request.user_register_request_inf_dto import UserRegisterRequestInfDto
from src.auth.application.dtos.request.user_register_request_dto import UserRegisterRequestDto
from src.common.application import ExceptionDecorator

class UserRegisterController:
    def __init__(self, app: FastAPI):
        self.app = app
        self.user_register_service = None
        self.setup_routes()

    async def init(self):
        session_generator = PostgresDatabase().get_session()
        session = await anext(session_generator)
        user_query_repository = OrmUserQueryRepository(session)
        user_command_repository = OrmUserCommandRepository(session)
        encryptor = BcryptEncryptor()
        id_generator = UuidGenerator()

        self.user_register_service = UserRegisterService(
            user_query_repository,
            user_command_repository,
            encryptor,
            id_generator
        )

    def setup_routes(self):
        @self.app.post("/register")
        async def register_user(user: UserRegisterRequestInfDto, token = Security(UserRoleVerify(), scopes=["client:read"])):

            if self.user_register_service is None:
                raise RuntimeError("UserRegisterService not initialized. Did you forget to call init()?")

            service = ExceptionDecorator(self.user_register_service)

            request = UserRegisterRequestDto(
                email=user.email,
                name=user.name,
                password=user.password,
                role=user.role
            )

            response = await service.execute(request)

            return None