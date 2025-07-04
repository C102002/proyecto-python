from datetime import time

class CreateRestaurantRequestDTO:
    def __init__(
        self,
        lat: float,
        lng: float,
        name: str,
        opening_time: time,
        closing_time: time
    ):
        self.lat = lat
        self.lng = lng
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time

    def __repr__(self):
        return (
            f"CreateRestaurantRequestDTO(lat={self.lat!r}, "
            f"lng={self.lng!r}, name={self.name!r}, "
            f"opening_time={self.opening_time!r}, "
            f"closing_time={self.closing_time!r})"
        )
