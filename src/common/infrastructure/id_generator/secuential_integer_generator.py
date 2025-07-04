import itertools
from src.common.application.id_generator.id_generator import IIdGenerator

class SequentialIntegerGenerator(IIdGenerator):
    def __init__(self, start: int = 1):
        self._counter = itertools.count(start)

    def generate_id(self) -> str:
        return str(next(self._counter))
