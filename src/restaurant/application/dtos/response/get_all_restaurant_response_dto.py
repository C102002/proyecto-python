from datetime import time

class GetAllRestaurantResponseDTO:
    def __init__(
        self,
        id: str,
        lat: float,
        lng: float,
        name: str,
        opening_time: time,
        closing_time: time,
    ):
        self.id = id
        self.lat = lat
        self.lng = lng
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time

    def __repr__(self):
        return (
            f"GetAllRestaurantResponseDTO("
            f"id={self.id!r}, "
            f"lat={self.lat!r}, "
            f"lng={self.lng!r}, "
            f"name={self.name!r}, "
            f"opening_time={self.opening_time!r}, "
            f"closing_time={self.closing_time!r}, "
            f")"
        )
