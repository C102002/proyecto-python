from pydantic import BaseModel, Field

class GetOccupancyPercentageResponseInfDTO(BaseModel):
    """
    Infrastructure DTO for the occupancy percentage response per restaurant.
    """

    restaurant_id: str = Field(..., description="Restaurant unique identifier")
    restaurant_name: str = Field(..., description="Name of the restaurant")
    occupied_tables: int = Field(..., description="Number of occupied tables")
    total_tables: int = Field(..., description="Total number of tables")
    occupancy_percent: float = Field(
        ...,
        description="Occupancy percentage (occupied_tables / total_tables * 100)"
    )

    class Config:
        title = "GetOccupancyPercentageResponseInfDTO"
