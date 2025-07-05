from pydantic import BaseModel, Field

class CreateReservationRequestController(BaseModel):
    date_start: str = Field(...)
    date_end: str = Field(...)
    client_id: str = Field(...)
    