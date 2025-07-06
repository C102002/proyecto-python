from src.common.utils.base_exception import BaseException

class InvalidMenuIdException(BaseException):
    def __init__(self, menu_id: str):
        super().__init__(f"Invalid menu id: {menu_id}")
