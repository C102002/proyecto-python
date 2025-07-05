from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_table_number_id_exception import InvalidTableNumberIdException

class TableNumberId(ValueObjectRoot["TableNumberId"]):
    def __init__(self, table_number_id: int):
        
        if table_number_id==0:
            raise InvalidTableNumberIdException(table_number_id=table_number_id)
        
        self.__table_number_id = table_number_id

    def equals(self, value: "TableNumberId") -> bool:
        return self.__table_number_id == value.__table_number_id
    
    @property
    def table_number_id(self) -> int:
        return self.__table_number_id
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(table_number_id={self.__table_number_id})"