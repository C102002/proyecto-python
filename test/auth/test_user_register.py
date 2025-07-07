import pytest
from test.auth.dto.user_register_request_mock_dto import UserRegisterRequestMockDto
from src.auth.application.dtos.request.user_register_request_dto import UserRegisterRequestDto
from fastapi import HTTPException

@pytest.mark.asyncio
async def test_user_register_success(user_register_service):

    request = UserRegisterRequestDto(
        email="test@example.com",
        name="Test User",
        password="strongpassword123"
    )

    response = await user_register_service.execute(request)
    
    assert response.is_error == False

@pytest.mark.asyncio
async def test_user_register_failure_by_role(user_register_service, user_repositories):
    request = UserRegisterRequestMockDto(
        email="test.role@example.com",
        name="Test User",
        password="strongpassword123",
        role="ADMIN"
    )
    user_query_repository, _ = user_repositories
    response = await user_register_service.execute(request)

    assert response.is_error == False
    user = await user_query_repository.get_user_email(request.email)
    assert user.value is not None
    assert user.value.role.role == "CLIENT"

    

@pytest.mark.asyncio
async def test_user_register_failure_by_email_existing(user_register_service):
    
    request = UserRegisterRequestDto(
        email="test@example.com",
        name="Daniel",
        password="strongpassword123"
    )

    status_code = 0

    try:
        response = await user_register_service.execute(request)
    except HTTPException as e:
        status_code = e.status_code
    
    assert status_code == 409