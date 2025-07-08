from pydantic import BaseModel, Field

from src.dashboard.application.enum.period_type import PeriodType
from src.dashboard.application.dtos.request.get_reservation_count_request_dto import (
    GetReservationCountRequestDTO,
)


class GetReservationCountRequestInfDTO(BaseModel):
    """
    Infrastructure DTO to parse the `period_type` query param
    for the reservation count endpoint.
    """

    period_type: PeriodType = Field(
        ...,
        description="Period to group reservations by: DAY or WEEK",
    )

    def to_dto(self) -> GetReservationCountRequestDTO:
        """
        Convert infra-layer DTO into application-layer DTO.
        """
        return GetReservationCountRequestDTO(period_type=self.period_type)
    
    class Config:
        title = "GetReservationCountRequestInfDTO"
        use_enum_values = True
