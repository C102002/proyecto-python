from datetime import time, date
from pydantic import BaseModel, Field
class CreateReservationInfRequestDto(BaseModel):
    date_start: time = Field(...)
    date_end: time = Field(...)
    reservation_date: date = Field(...)
    table_number_id: str = Field(...)
    restaurant_id: str = Field(...)
    dish_id: list[str] = Field(...)
    