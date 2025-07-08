from pydantic import BaseModel, Field

class AdminCancelReservationInfRequestDto(BaseModel):
    reservation_id: str = Field(...)
    