from src.dashboard.application.enum.period_type import PeriodType

class GetReservationCountRequestDTO:
    """
    DTO to retrieve the total number of reservations,
    grouped by the specified period type.
    """

    def __init__(self, period_type: PeriodType):
        self.period_type = period_type

    def __repr__(self):
        return f"GetReservationCountRequestDTO(period_type={self.period_type!r})"
