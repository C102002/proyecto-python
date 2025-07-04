from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel
from sqlalchemy.orm import relationship
from enum import Enum

from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum

class OrmTableModel(SQLModel, table=True):
    __tablename__  = "table"
    id: Optional[int] = Field(default=None, primary_key=True)
    capacity: int = Field(ge=2, le=12, nullable=False)
    location: TableLocationEnum = Field(nullable=False)
    restaurant_id: str = Field(foreign_key="restaurant.id", nullable=False)