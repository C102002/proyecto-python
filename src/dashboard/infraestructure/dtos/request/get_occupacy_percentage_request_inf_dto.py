from pydantic import BaseModel, Field

from src.dashboard.application.dtos.request.get_occupacy_percentage_request_dto import GetOccupancyPercentageRequestDto


class GetOccupancyPercentageRequestInfDTO(BaseModel):
    """
    Infra DTO to parse pagination query params for occupancy endpoint.
    """

    page: int = Field(
        1,
        ge=1,
        description="Page number (1-indexed)"
    )
    per_page: int = Field(
        10,
        ge=1,
        description="Number of items per page"
    )

    def to_dto(self) -> GetOccupancyPercentageRequestDto:
        """
        Convert infra DTO into application-layer DTO.
        """
        return GetOccupancyPercentageRequestDto(
            page=self.page,
            per_page=self.per_page
        )
