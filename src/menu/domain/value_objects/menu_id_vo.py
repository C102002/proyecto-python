from src.common.domain.value_object.value_object_root import ValueObjectRoot
from src.menu.domain.domain_exceptions.invalid_menu_id_exception import InvalidMenuIdException
import uuid

class MenuIdVo(ValueObjectRoot["MenuIdVo"]):
    def __init__(self, value: str | None = None):
        if value is None:
            self.__value = str(uuid.uuid4())
        else:
            try:
                self.__value = str(uuid.UUID(value))
            except ValueError:
                raise InvalidMenuIdException(value)
        
    def equals(self, value: "MenuIdVo") -> bool:
        return self.__value == value.__value
    
    @property
    def value(self) -> str:
        return self.__value
