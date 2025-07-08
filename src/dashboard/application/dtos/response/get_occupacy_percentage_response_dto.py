class GetOccupancyPercentageResponseDto:
    """
    Percentage of occupancy per restaurant for a given period.
    """

    def __init__(
        self,
        restaurant_id: str,
        restaurant_name: str,
        occupied_tables: int,
        total_tables: int,
        occupancy_percent: float,
    ):
        self.restaurant_id = restaurant_id
        self.restaurant_name = restaurant_name
        self.occupied_tables = occupied_tables
        self.total_tables = total_tables
        self.occupancy_percent = occupancy_percent

    def __repr__(self):
        return (
            f"GetOccupancyPercentageResponseDto("
            f"restaurant_id={self.restaurant_id!r}, "
            f"restaurant_name={self.restaurant_name!r}, "
            f"occupied_tables={self.occupied_tables!r}, "
            f"total_tables={self.total_tables!r}, "
            f"occupancy_percent={self.occupancy_percent!r}"
            f")"
        )
