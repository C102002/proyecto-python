import pytest
from src.auth.application.dtos.request.user_login_request_dto import UserLoginRequestDto
from src.auth.application.dtos.request.user_register_request_dto import UserRegisterRequestDto
from fastapi import HTTPException



@pytest.mark.order(1)
@pytest.mark.asyncio
async def test_user_login_success(user_login_service, user_register_service):
    
    request = UserRegisterRequestDto(
        email="test.login@example.com",
        password="strongpassword123",
        name="Andres"
    )

    response = await user_register_service.execute(request)

    assert response.is_error == False

    request = UserLoginRequestDto(
        email="test.login@example.com",
        password="strongpassword123"
    )
    
    response = await user_login_service.execute(request)
    
    assert response.is_error == False
    assert response.value.token is not None

@pytest.mark.asyncio
async def test_user_login_failure_by_password(user_login_service):
    request = UserLoginRequestDto(
        email="test.login@example.com",
        password="12345"
    )

    status_code = 0

    try: 
        response = await user_login_service.execute(request)
    except HTTPException as e:
        status_code = e.status_code
    
    assert status_code == 403