from datetime import time
from typing import Optional

class UpdateRestaurantRequestDTO:
    def __init__(
        self,
        id: str = None,
        lat: Optional[float] = None,
        lng: Optional[float] = None,
        name: Optional[str] = None,
        opening_time: Optional[time] = None,
        closing_time: Optional[time] = None,
    ):
        """
        DTO for updating a restaurant. All fields are optional—
        only provided values will be applied.

        :param id: UUID of the restaurant
        :param lat: New latitude
        :param lng: New longitude
        :param name: New restaurant name
        :param opening_time: New opening time
        :param closing_time: New closing time
        """
        self.id = id
        self.lat = lat
        self.lng = lng
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time

    def __repr__(self):
        return (
            f"UpdateRestaurantRequestDTO("
            f"id={self.id!r}, "
            f"lat={self.lat!r}, "
            f"lng={self.lng!r}, "
            f"name={self.name!r}, "
            f"opening_time={self.opening_time!r}, "
            f"closing_time={self.closing_time!r}"
            f")"
        )
