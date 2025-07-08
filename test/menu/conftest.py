import pytest
from src.common.application import IService, ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from test.mocks.menu.repositories.menu_store import menu_store

from src.menu.application.dtos.request.create_dish_request_dto import CreateDishRequestDto
from src.menu.domain.entities.dish import Dish
from src.menu.application.services.add_dish_to_menu_service import AddDishToMenuService
from src.menu.domain.aggregate.menu import Menu
from test.mocks.menu.repositories.query.menu_query_repository_mock import MenuQueryRepositoryMock
from test.mocks.menu.repositories.command.menu_command_repository_mock import MenuCommandRepositoryMock

@pytest.fixture(scope="session")
def menu_shared_data() -> list[Menu]:
    return menu_store

@pytest.fixture(scope="session")
def menu_repositories(menu_shared_data) -> tuple[MenuQueryRepositoryMock, MenuCommandRepositoryMock]:
    return (
        MenuQueryRepositoryMock(menu_shared_data),
        MenuCommandRepositoryMock(menu_shared_data)
    )

@pytest.fixture(scope="function")
def add_dish_to_menu_service(menu_repositories) -> IService[CreateDishRequestDto, Dish]:
    query_repo, command_repo = menu_repositories
    return ExceptionDecorator(
        service=AddDishToMenuService(    
            menu_command_repository=command_repo,
            menu_query_repository=query_repo
        ),
        error_handler=FastApiErrorHandler()
    )