from datetime import time

class CreateRestaurantResponseDTO:
    def __init__(
        self,
        id:str,
        lat: float,
        lng: float,
        name: str,
        opening_time: time,
        closing_time: time
    ):
        self.id = id
        self.lat = lat
        self.lng = lng
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time

    def __repr__(self):
        return (
            f"CreateRestaurantRequestDTO(id={self.id!r}"
            f"lat={self.lat!r}, "
            f"lng={self.lng!r}, name={self.name!r}, "
            f"opening_time={self.opening_time!r}, "
            f"closing_time={self.closing_time!r})"
        )
