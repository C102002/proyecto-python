from src.dashboard.application.enum.period_type import PeriodType

class GetReservationCountResponseDTO:
    """
    Total number of reservations grouped by period.
    """

    def __init__(self, period_type: PeriodType, count: int):
        self.period_type = period_type
        self.count = count

    def __repr__(self):
        return (
            f"GetReservationCountResponseDTO("
            f"period_type={self.period_type!r}, "
            f"count={self.count!r}"
            f")"
        )
