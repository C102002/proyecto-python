from src.common.application import IService
from src.common.utils import Result
from ..dtos.request.user_update_request_dto import UserUpdateRequestDto
from ..repositories.query.user_query_repository import IUserQueryRepository
from ..repositories.command.user_command_repository import IUserCommandRepository
from ..encryptor.encryptor import IEncryptor
from src.common.utils import Result
from src.auth.domain.value_objects.user_email_vo import UserEmailVo
from src.auth.domain.value_objects.user_name_vo import UserNameVo
from src.auth.domain.value_objects.user_password_vo import UserPasswordVo
from ..exceptions.user_already_exists_exception import UserAlreadyExistsException

class UserUpdateService(IService[UserUpdateRequestDto, None]):

    def __init__(self, user_query_repository: IUserQueryRepository, user_command_repository: IUserCommandRepository, encryptor: IEncryptor):
        super().__init__()
        self.user_query_repository = user_query_repository
        self.user_command_repository = user_command_repository
        self.encryptor = encryptor

    async def execute(self, value: UserUpdateRequestDto) -> Result[None]:
        user = await self.user_query_repository.get_by_id(value.id)

        if (user.is_error):
            return Result.fail(user.error)
        
        user_updated = user.value

        if value.email:
            user_finded = await self.user_query_repository.exists_user_by_email(value.email)

            if (user_finded.is_error):
                return Result.fail(user_finded.error)

            if (user_finded.value):
                return Result.fail(UserAlreadyExistsException(value.email))

            user_updated.update_email(UserEmailVo(value.email))

        if value.name:
            user_updated.update_name(UserNameVo(value.name))

        if value.password:
            password_encrypted = self.encryptor.encrypt(value.password)
            user_updated.update_password(UserPasswordVo(password_encrypted))

        save = await self.user_command_repository.update(user_updated)

        if (save.is_error):
            return Result.fail(save.error)
        
        return Result.success(None)