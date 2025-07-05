from pydantic import BaseModel, Field

class CancelReservationRequestController(BaseModel):
    reservation_id: str = Field(...)
    