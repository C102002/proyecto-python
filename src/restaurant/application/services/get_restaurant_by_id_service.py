from src.common.application import IService
from src.common.utils import Result
from src.restaurant.application.dtos.response.create_table_response_dto import CreateTableResponseDTO
from src.restaurant.application.repositories.query.restaurant_query_repository import IRestaurantQueryRepository
from ..dtos.request.get_restaurant_by_id_request_dto import GetRestaurantByIdRequestDTO
from ..dtos.response.get_restaurant_by_id_response_dto import GetRestaurantByIdResponseDTO

class GetRestaurantByIdService(IService[GetRestaurantByIdRequestDTO, GetRestaurantByIdResponseDTO]):

    def __init__(self, restaurant_query_repository: IRestaurantQueryRepository):
        super().__init__()
        self.restaurant_query_repository = restaurant_query_repository

    async def execute(self, value: GetRestaurantByIdRequestDTO) -> Result[GetRestaurantByIdResponseDTO]:
        
        
        response_repo=await self.restaurant_query_repository.get_by_id(restaurant_id=value.restaurant_id)
        
        if response_repo.is_error:
            return Result.fail(response_repo.error)
        
        restaurant=response_repo.value
        
        for tables in restaurant.tables:
            print(f"table domain : {tables}")

        
        return Result.success(
            GetRestaurantByIdResponseDTO(
                id=restaurant.id.restaurant_id,
                lat=restaurant.location.lat,
                lng=restaurant.location.lng,
                name=restaurant.name.name,
                opening_time=restaurant.opening_time.opening_time,
                closing_time=restaurant.closing_time.closing_time,
                tables=[
                    CreateTableResponseDTO(
                        id=tables.id.table_number_id,
                        location=tables.location.location.value,
                        capacity=tables.capacity.capacity,
                        restaurant_id=restaurant.id.restaurant_id
                    )
                    for tables in restaurant.tables
                ]
            )
        )

