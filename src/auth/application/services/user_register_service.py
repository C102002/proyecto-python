from src.common.application import IService
from src.common.utils import Result
from ..dtos.request.user_register_request_dto import UserRegisterRequestDto
from ..repositories.query.user_query_repository import IUserQueryRepository
from ..repositories.command.user_command_repository import IUserCommandRepository
from ..encryptor.encryptor import IEncryptor
from ..exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.common.utils import Result
from src.common.application import IIdGenerator
from src.auth.domain.aggregate.user import User
from src.auth.domain.aggregate.user import UserEmailVo
from src.auth.domain.aggregate.user import UserIdVo
from src.auth.domain.aggregate.user import UserNameVo
from src.auth.domain.aggregate.user import UserPasswordVo
from src.auth.domain.aggregate.user import UserRoleVo

class UserRegisterService(IService[UserRegisterRequestDto, None]):

    def __init__(self, user_query_repository: IUserQueryRepository, user_command_repository: IUserCommandRepository, encryptor: IEncryptor, id_generator: IIdGenerator):
        super().__init__()
        self.user_query_repository = user_query_repository
        self.user_command_repository = user_command_repository
        self.encryptor = encryptor
        self.id_generator = id_generator
    
    async def execute(self, value: UserRegisterRequestDto) -> Result[None]:
        user_finded = await self.user_query_repository.exists_user_by_email(value.email)

        if (user_finded.is_error):
            return Result.fail(user_finded.error)

        if (user_finded.value):
            return Result.fail(UserAlreadyExistsException(value.email))
        
        user_id = self.id_generator.generate_id()

        password_hashed = self.encryptor.encrypt(value.password)

        new_user = User(
            UserIdVo(user_id),
            UserEmailVo(value.email),
            UserNameVo(value.name),
            UserPasswordVo(password_hashed),
            UserRoleVo(value.role)
        )

        user_saved = await self.user_command_repository.save(new_user)

        if (user_saved.is_error):
            return Result.fail(user_saved.error)
        
        return Result.success(None)

