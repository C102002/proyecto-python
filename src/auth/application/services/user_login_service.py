from src.common.application import IService
from src.common.utils import Result
from ..repositories.query.user_query_repository import IUserQueryRepository
from ..dtos.request.user_login_request_dto import UserLoginRequestDto
from ..dtos.response.user_login_response_dto import UserLoginResponseDto
from ..encryptor.encryptor import IEncryptor
from ..exceptions.invalid_credentials_exception import InvalidCredentialsException
from src.common.application import ITokenGenerator

class UserLoginService(IService[UserLoginRequestDto, UserLoginResponseDto]):

    def __init__(self, user_query_repository: IUserQueryRepository, encryptor: IEncryptor, token_generator: ITokenGenerator):
        super().__init__()
        self.user_query_repository = user_query_repository
        self.encryptor = encryptor
        self.token_generator = token_generator

    async def execute(self, value: UserLoginRequestDto) -> Result[UserLoginResponseDto]:
        
        user = await self.user_query_repository.get_user_email(value.email)

        if (user.is_error):
            return Result.fail(user.error)

        if (self.encryptor.verify_password(value.password, user.value.password.password) != True):
            return Result.fail(InvalidCredentialsException())

        token = self.token_generator.generate_token({"sub": user.value.email.email})
        response = UserLoginResponseDto(
            token=token
        )

        return Result.success(response)

