from sqlmodel import Field, SQLModel
from datetime import time, date

class OrmReservationModel(SQLModel, table=True):

    __tablename__ = "reservation"

    id: str = Field(nullable=False, primary_key=True, unique=True)
    date_start: time = Field(nullable=False, index=True)
    date_end: time = Field(nullable=False, index=True)
    client_id: str = Field(nullable=False, index=True)
    status: str = Field(nullable=False)
    table_number_id: str = Field(nullable=False)
    reservation_date: date = Field(nullable=False, index=True)
    restaurant_id: str = Field(nullable=False)
    
    def create_reservation(self, id: str, dateStart: str, dateEnd: str, clientID: str, status: str, reservation_date: date, table_number_id: str, restaurant_id: str) -> "OrmReservationModel":
        return OrmReservationModel(
            id=id,
            date_end=dateEnd,
            date_start=dateStart,
            status=status,
            client_id=clientID,
            reservation_date = reservation_date,
            table_number_id=table_number_id,
            restaurant_id=restaurant_id
        )