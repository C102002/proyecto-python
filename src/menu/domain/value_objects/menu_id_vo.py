from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_menu_id_exception import InvalidMenuIdException
import uuid

class MenuIdVo(ValueObjectRoot[uuid.UUID]):
    def __init__(self, value: str = None):
        if value is None:
            value = str(uuid.uuid4())
        try:
            super().__init__(uuid.UUID(value))
        except ValueError:
            raise InvalidMenuIdException(value)
