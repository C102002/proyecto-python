from datetime import time
from pydantic import BaseModel, Field
class CreateReservationRequestController(BaseModel):
    date_start: time = Field(...)
    date_end: time = Field(...)
    client_id: str = Field(...)
    