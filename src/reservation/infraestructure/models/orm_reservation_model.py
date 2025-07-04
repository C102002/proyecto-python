from sqlmodel import Field, SQLModel

class OrmReservationModel(SQLModel, table=True):

    __tablename__ = "reservation" # type: ignore

    id: str = Field(nullable=False, primary_key=True, unique=True)
    dateStart: str = Field(nullable=False, index=True)
    dateEnd: str = Field(nullable=False, index=True)
    clientID: str = Field(nullable=False, index=True)
    status: str = Field(nullable=False)
    
    def create_reservation(self, id: str, dateStart: str, dateEnd: str, clientID: str, status: str) -> "OrmReservationModel":
        return OrmReservationModel(
            id=id,
            dateEnd=dateEnd,
            dateStart=dateStart,
            status=status,
            clientID=clientID
        )