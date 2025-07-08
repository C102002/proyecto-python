from pydantic import BaseModel, Field

class GetTopDishesPreorderResponseInfDTO(BaseModel):
    """
    Infrastructure DTO for the top pre-ordered dishes response.
    """

    dish_id: str = Field(
        ...,
        description="Dish unique identifier"
    )
    dish_name: str = Field(
        ...,
        description="Name of the dish"
    )
    total_preorders: int = Field(
        ...,
        ge=0,
        description="Total number of times the dish was pre-ordered"
    )

    class Config:
        title = "GetTopDishesPreorderResponseInfDTO"
