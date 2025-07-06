from enum import Enum

class TableLocationEnum(str, Enum):
    terraza         = "terraza"
    interior        = "interior"
    parque          = "parque"
    jard_interno    = "jardín interno"
    jard_externo    = "jardín externo"
