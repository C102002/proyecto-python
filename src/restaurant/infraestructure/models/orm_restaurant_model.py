from datetime import time

from sqlmodel import SQLModel, Field


class OrmRestaurantModel(SQLModel, table=True):
    
    __tablename__ = "restaurant" # type: ignore
    
    id: str = Field(
        primary_key=True,
        nullable=False,
        unique=True,
        index=True,
        description="UUID único del restaurante"
    )
    lat: float = Field(
        nullable=False,
        description="Latitud del restaurante"
    )
    lng: float = Field(
        nullable=False,
        description="Longitud del restaurante"
    )
    name: str = Field(
        nullable=False,
        description="Nombre del restaurante"
    )
    opening_time: time = Field(
        nullable=False,
        description="Hora de apertura (HH:MM:SS)"
    )
    closing_time: time = Field(
        nullable=False,
        description="Hora de cierre (HH:MM:SS)"
    )
