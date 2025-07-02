from fastapi import FastAPI, Security, Depends
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

class UserRegisterController:
    def __init__(self, app: FastAPI):
        self.app = app
        
        self.setup_routes()

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
        @self.app.post("/register")
        async def register_user(user: UserRegisterRequestInfDto, token = Security(UserRoleVerify(), scopes=["client:read"]), register_service: UserRegisterService = Depends(self.get_service)):

            if register_service is None:
                raise RuntimeError("UserRegisterService not initialized. Did you forget to call init()?")

            service = ExceptionDecorator(register_service)

            request = UserRegisterRequestDto(
                email=user.email,
                name=user.name,
                password=user.password,
                role=user.role
            )

            response = await service.execute(request)

            return None