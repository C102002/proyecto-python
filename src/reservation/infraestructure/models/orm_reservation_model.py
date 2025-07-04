from sqlmodel import Field, SQLModel

class OrmReservationModel(SQLModel, table=True):

    __tablename__ = "reservation" # type: ignore

    id: str = Field(nullable=False, primary_key=True, unique=True)
    date_start: str = Field(nullable=False, index=True)
    date_end: str = Field(nullable=False, index=True)
    client_id: str = Field(nullable=False, index=True)
    status: str = Field(nullable=False)
    
    def create_reservation(self, id: str, dateStart: str, dateEnd: str, clientID: str, status: str) -> "OrmReservationModel":
        return OrmReservationModel(
            id=id,
            date_end=dateEnd,
            date_start=dateStart,
            status=status,
            client_id=clientID
        )