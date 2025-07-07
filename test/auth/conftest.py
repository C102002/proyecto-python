import pytest
from test.mocks.auth.repositories.command.user_command_repository_mock import UserCommandRepositoryMock
from test.mocks.auth.repositories.query.user_query_repository_mock import UserQueryRepositoryMock
from src.common.infrastructure import UuidGenerator, JwtGenerator
from src.auth.infrastructure.encryptor.bcrypt_encryptor import BcryptEncryptor
from src.auth.application.services.user_register_service import UserRegisterService
from src.auth.application.services.user_login_service import UserLoginService
from src.common.application import IService, ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.auth.application.dtos.request.user_register_request_dto import UserRegisterRequestDto
from src.auth.application.dtos.request.user_login_request_dto import UserLoginRequestDto
from src.auth.application.dtos.response.user_login_response_dto import UserLoginResponseDto
from src.auth.domain.aggregate.user import User
from test.mocks.auth.repositories.user_store import user_store

@pytest.fixture(scope="session")
def shared_user_list() -> list[User]:
    return user_store

@pytest.fixture(scope="session")
def user_repositories(shared_user_list) -> tuple[UserQueryRepositoryMock, UserCommandRepositoryMock]:
    return (
        UserQueryRepositoryMock(shared_user_list),
        UserCommandRepositoryMock(shared_user_list)
    )

@pytest.fixture(scope="function")
def user_register_service(user_repositories) -> IService[UserRegisterRequestDto, None]:
    user_query_repository, user_command_repository = user_repositories
    return ExceptionDecorator(
        service=UserRegisterService(
            user_query_repository=user_query_repository,
            user_command_repository=user_command_repository,
            encryptor=BcryptEncryptor(),
            id_generator=UuidGenerator()
        ),
        error_handler=FastApiErrorHandler()
    )

@pytest.fixture(scope="function")
def user_login_service(user_repositories) -> IService[UserLoginRequestDto, UserLoginResponseDto]:
    user_query_repository, _ = user_repositories
    return ExceptionDecorator(
        service=UserLoginService(
            user_query_repository=user_query_repository,
            encryptor=BcryptEncryptor(),
            token_generator=JwtGenerator()
        ),
        error_handler=FastApiErrorHandler()
    )