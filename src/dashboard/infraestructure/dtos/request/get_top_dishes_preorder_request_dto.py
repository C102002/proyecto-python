from pydantic import BaseModel, Field

from src.dashboard.application.dtos.request.get_top_dishes_preorder_request_dto import (
    GetTopDishesPreorderRequestDTO,
)


class GetTopDishesPreorderRequestInfDTO(BaseModel):
    """
    Infrastructure DTO to parse the `top_n` query param 
    for the top pre-ordered dishes endpoint.
    """

    top_n: int = Field(
        5,
        ge=1,
        description="Number of top pre-ordered dishes to retrieve"
    )

    def to_dto(self) -> GetTopDishesPreorderRequestDTO:
        """
        Convert infra-layer DTO into application-layer DTO.
        """
        return GetTopDishesPreorderRequestDTO(top_n=self.top_n)
