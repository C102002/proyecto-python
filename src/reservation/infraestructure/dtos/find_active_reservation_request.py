from pydantic import BaseModel, Field

class FindActiveReservationRequestController(BaseModel):
    client_id: str = Field(...)
    