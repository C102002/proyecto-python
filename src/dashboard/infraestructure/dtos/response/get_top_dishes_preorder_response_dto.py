from pydantic import BaseModel, Field

from src.dashboard.application.enum.period_type import PeriodType

class GetReservationCountResponseInfDTO(BaseModel):
    """
    Infrastructure DTO for the reservation count response.
    """

    period_type: PeriodType = Field(
        ...,
        description="Period to group reservations by: DAY or WEEK"
    )
    count: int = Field(
        ...,
        ge=0,
        description="Total number of reservations in the given period"
    )

    class Config:
        title = "GetReservationCountResponseInfDTO"
        use_enum_values = True
