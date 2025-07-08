import pytest
from test.mocks.restaurant.repositories.command.restaurant_command_repository_mock import RestaurantCommandRepositoryMock
from test.mocks.restaurant.repositories.query.restaurant_query_repository_mock import RestaurantQueryRepositoryMock
from src.common.infrastructure import UuidGenerator
from src.common.infrastructure.id_generator.secuential_integer_generator import SequentialIntegerGenerator
from src.common.application import IService, ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from src.restaurant.domain.aggregate.restaurant import Restaurant
from test.mocks.restaurant.repositories.restaurant_store import restaurant_store
from src.restaurant.application.dtos.request.create_restaurant_request_dto import CreateRestaurantRequestDTO
from src.restaurant.application.dtos.response.create_restaurant_response_dto import CreateRestaurantResponseDTO
from src.restaurant.application.services.create_restaurant_service import CreateRestaurantService

@pytest.fixture(scope="session")
def shared_restaurant_list() -> list[Restaurant]:
    return restaurant_store

@pytest.fixture(scope="session")
def restaurant_repositories(shared_restaurant_list) -> tuple[RestaurantQueryRepositoryMock, RestaurantCommandRepositoryMock]:
    return (
        RestaurantQueryRepositoryMock(shared_restaurant_list),
        RestaurantCommandRepositoryMock(shared_restaurant_list)
    )

@pytest.fixture(scope="function")
def create_restaurant_service(restaurant_repositories) -> IService[CreateRestaurantRequestDTO, CreateRestaurantResponseDTO]:
    _, restaurant_command_repository = restaurant_repositories
    return ExceptionDecorator(
        service=CreateRestaurantService(
            restaurant_command_repository=restaurant_command_repository,
            id_generator=UuidGenerator(),
            tables_id_generator=SequentialIntegerGenerator()
        ),
        error_handler=FastApiErrorHandler()
    )