from pydantic import BaseModel, Field

class AdminCancelReservationRequestController(BaseModel):
    reservation_id: str = Field(...)
    