import pytest
from src.common.infrastructure import UuidGenerator
from src.common.application import IService, ExceptionDecorator
from src.common.infrastructure.error_handler.fast_api_error_handler import FastApiErrorHandler
from test.mocks.reservation.repositories.reservation_store import reservation_store

from src.reservation.application.dtos.request.cancel_reservation_request_dto import CancelReservationRequest
from src.reservation.application.dtos.response.cancel_reservation_response_dto import CancelReservationResponse
from src.reservation.application.dtos.request.create_reservation_request_dto import CreateReservationRequest
from src.reservation.application.dtos.response.create_reservation_response_dto import CreateReservationResponse
from src.reservation.application.services.cancel_reservation_service import CancelReservationService
from src.reservation.application.services.create_reservation_service import CreateReservationService
from src.reservation.domain.aggregate.reservation import Reservation
from test.mocks.reservation.repositories.query.reservation_query_repository_mock import ReservationQueryRepositoryMock
from test.mocks.reservation.repositories.command.reservation_command_repository_mock import ReservationCommandRepositoryMock
from test.mocks.restaurant.repositories.query.restaurant_query_repository_mock  import RestaurantQueryRepositoryMock
from test.mocks.restaurant.repositories.restaurant_store import restaurant_store
from src.restaurant.domain.aggregate.restaurant import Restaurant
from test.restaurant.conftest import create_restaurant_service, shared_restaurant_list, restaurant_repositories

@pytest.fixture(scope="session")
def shared_data() -> list[Reservation]:
    return reservation_store

@pytest.fixture(scope="session")
def restau_data() -> list[Restaurant]:
    return restaurant_store

@pytest.fixture(scope="session")
def reser_repositories(shared_data, restau_data) -> tuple[ReservationQueryRepositoryMock, ReservationCommandRepositoryMock, RestaurantQueryRepositoryMock]:
    return (
        ReservationQueryRepositoryMock(shared_data),
        ReservationCommandRepositoryMock(shared_data),
        RestaurantQueryRepositoryMock(restau_data),
    )

@pytest.fixture(scope="function")
def create_reservation_service(reser_repositories) -> IService[CreateReservationRequest, CreateReservationResponse]:
    query_repo, command_repo, query_restau = reser_repositories
    return ExceptionDecorator(
        service=CreateReservationService(    
            # query_restau= query_restau,
            query_reser=query_repo,
            command_reser=command_repo,
            query_restau=query_restau,
            id_generator=UuidGenerator()
        ),
        error_handler=FastApiErrorHandler()
    )

@pytest.fixture(scope="function")
def cancel_reservation(reser_repositories) -> IService[CancelReservationRequest, CancelReservationResponse]:
    query_repo, command_repo, _ = reser_repositories
    return ExceptionDecorator(
        service=CancelReservationService(
            query_reser= query_repo, 
            command_reser= command_repo
        ),
        error_handler=FastApiErrorHandler()
    )
    