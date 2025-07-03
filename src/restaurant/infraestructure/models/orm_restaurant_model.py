from __future__ import annotations
from datetime import time
from typing import List

from sqlmodel import Relationship, SQLModel, Field


class OrmRestaurantModel(SQLModel, table=True):
    __tablename__ = "restaurant"
    
    id: str = Field(primary_key=True, index=True, nullable=False, unique=True)
    lat: float = Field(nullable=False)
    lng: float = Field(nullable=False)
    name: str = Field(nullable=False)
    opening_time : time  = Field(nullable=False)
    closing_time : time = Field(nullable=False)
    tables : List["OrmTableModel"] = Relationship(
                       back_populates="restaurant",
                       sa_relationship_kwargs={"cascade":"all, delete-orphan"}
                   )