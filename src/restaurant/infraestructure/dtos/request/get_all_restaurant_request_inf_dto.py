from pydantic import BaseModel, Field

class GetAllRestaurantRequestInfDTO(BaseModel):
    page: int = Field(
        1,
        ge=1,
        description="Número de página (1-indexed)"
    )
    size: int = Field(
        10,
        ge=1,
        description="Cantidad de restaurantes por página"
    )

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size

    @property
    def limit(self) -> int:
        return self.size

    class Config:
        title = "GetAllRestaurantRequestInfDTO"
