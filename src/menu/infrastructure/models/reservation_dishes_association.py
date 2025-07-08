from sqlmodel import Field, Relationship, SQLModel

class OrmReservationDishModel(SQLModel, table=True):
    __tablename__ = 'reservation_dish_association'

    reservation_id: str = Field(primary_key=True, foreign_key="reservation.id")
    dish_id: str = Field(primary_key=True, foreign_key="dishes.id")
    

    reservation: "OrmReservationModel" = Relationship(back_populates="dishes")
    dish: "DishModel" = Relationship(back_populates="reservations")