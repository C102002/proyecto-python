from __future__ import annotations
from datetime import time
from typing import List

from sqlmodel import SQLModel, Field, Relationship


class OrmRestaurantModel(SQLModel, table=True):
    __tablename__ = "restaurant"

    id: str        = Field(
        primary_key=True, index=True, nullable=False, unique=True
    )
    lat: float     = Field(nullable=False)
    lng: float     = Field(nullable=False)
    name: str      = Field(nullable=False)

    # Para campos de tipo time SQLModel crea automáticamente TIME
    opening_time: time = Field(nullable=False)
    closing_time: time = Field(nullable=False)
