from src.common.domain import DomainException

class InvalidTableNumberIdException(DomainException):
    
    def __init__(self, table_number_id: str):
        super().__init__(f"Invalid Table number Id: {table_number_id}, because its already in the resaturant registered")