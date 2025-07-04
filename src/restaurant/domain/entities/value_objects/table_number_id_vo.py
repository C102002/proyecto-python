from src.common.domain import ValueObjectRoot
from ..domain_exceptions.invalid_table_number_id_exception import InvalidTableNumberIdException

class TableNumberId(ValueObjectRoot["TableNumberId"]):
    def __init__(self, table_number_id: int):
        
        if table_number_id==0:
            InvalidTableNumberIdException()
        
        self.__table_number_id = table_number_id

    def equals(self, value: "TableNumberId") -> bool:
        return self.__table_number_id == value.__table_number_id
    
    @property
    def table_number_id(self) -> int:
        return self.__table_number_id