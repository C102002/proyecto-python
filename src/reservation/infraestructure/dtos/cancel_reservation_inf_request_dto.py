from pydantic import BaseModel, Field

class CancelReservationInfRequestDto(BaseModel):
    reservation_id: str = Field(...)    