# src/restaurant/infraestructure/models/orm_table_model.py
from __future__ import annotations
from typing      import Optional
from sqlalchemy import Column
from sqlmodel    import Field, SQLModel, Relationship
from sqlalchemy.types import Enum as SaEnum

from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum

class OrmTableModel(SQLModel, table=True):
    __tablename__  = "table"
    id : Optional[int] = Field(default=None, primary_key=True)
    number : int = Field(index=True, nullable=False)
    capacity : int = Field(ge=2, le=12, nullable=False)
    location : TableLocationEnum  = Field(
                        sa_column=Column(
                           SaEnum(TableLocationEnum, name="tablelocationenum"),
                           nullable=False
                        )
                    )
    restaurant_id : str  = Field(foreign_key="restaurant.id", nullable=False)
    restaurant : "OrmRestaurantModel" = Relationship(back_populates="tables")
