from datetime import date
from typing import NamedTuple

from src.dashboard.enum.period_type import PeriodType

class ReservationCountRequestDTO(NamedTuple):
    """
    Request para obtener el total de reservas,
    agrupadas según el tipo de periodo.
    """
    period_type: PeriodType   # DAY o WEEK
