from fastapi import FastAPI, Security, Depends
from src.common.infrastructure import GetPostgresqlSession
from ...middlewares.user_role_verify import UserRoleVerify
from src.auth.infrastructure.repositories.query.orm_user_query_repository import OrmUserQueryRepository
from src.auth.infrastructure.repositories.command.orm_user_command_repository import OrmUserCommandRepository
from src.auth.infrastructure.encryptor.bcrypt_encryptor import BcryptEncryptor
from src.auth.application.services.user_update_service import UserUpdateService
from ...dtos.request.user_update_request_inf_dto import UserUpdateRequestInfDto
from src.auth.application.dtos.request.user_update_request_dto import UserUpdateRequestDto
from src.common.application import ExceptionDecorator
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler

class UserUpdateController:
    def __init__(self, app: FastAPI):
        self.app = app
        
        self.setup_routes()

    async def get_service(self, postgres_session: AsyncSession = Depends(GetPostgresqlSession())):
        encryptor = BcryptEncryptor()
        orm_user_query_repository = OrmUserQueryRepository(postgres_session)
        orm_user_command_repository = OrmUserCommandRepository(postgres_session)

        user_update_service = UserUpdateService(
            orm_user_query_repository,
            orm_user_command_repository,
            encryptor
        )

        return user_update_service

    def setup_routes(self):
        @self.app.patch("/update")
        async def update_user(user: UserUpdateRequestInfDto, token = Security(UserRoleVerify(), scopes=["client:write_user", "admin:manage"]), update_service: UserUpdateService = Depends(self.get_service)):

            if update_service is None:
                raise RuntimeError("UserUpdateService not initialized. Did you forget to call init()?")

            service = ExceptionDecorator(update_service, FastApiErrorHandler())

            request = UserUpdateRequestDto(
                id=user.id,
                email=user.email,
                name=user.name,
                password=user.password,
            )

            await service.execute(request)

            return None