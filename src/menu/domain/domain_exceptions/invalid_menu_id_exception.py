from src.common.domain import DomainException

class InvalidMenuIdException(DomainException):
    def __init__(self, menu_id: str):
        super().__init__(f"Invalid menu id: {menu_id}")
