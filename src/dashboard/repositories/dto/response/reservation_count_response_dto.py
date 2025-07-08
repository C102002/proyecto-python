from datetime import date
from typing import NamedTuple

class ReservationCountResponseDTO(NamedTuple):
    """
    Número total de reservas agrupadas por período.
    """
    period: date      # día o fecha inicial de la semana
    count: int
