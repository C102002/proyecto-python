import uuid
from src.common.application import IIdGenerator

class UuidGenerator(IIdGenerator):
    
    def generate_id(self) -> str:
        return str(uuid.uuid4())