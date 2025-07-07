from src.common.domain.value_object.value_object_root import ValueObjectRoot

class DishImageVo(ValueObjectRoot[str]):
    def __init__(self, value: str):
        super().__init__(value)
