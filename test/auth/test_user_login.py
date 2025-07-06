from fastapi.testclient import TestClient
from src.main import app
import pytest
from dotenv import load_dotenv
import asyncio
import platform

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()

client = TestClient(app)

@pytest.mark.asyncio
async def test_user_login_success():
    user_data = {
        "email": "test2@example.com",
        "name": "Test User 2",
        "password": "strongpassword123"
    }
    # Test successful registration
    response = client.post("/auth/register", json=user_data)

    assert response.status_code == 201
    response_data = response.json()
    assert response_data is None

    user_data_login = {
        "username": "test2@example.com",
        "password": "strongpassword123"
    }
    response = client.post("/auth/login", data=user_data_login)
    
    print("STATUS:", response.status_code)
    print("BODY  :", response.text)

    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    assert "token_type" in response_data
    assert response_data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_user_login_failure_by_password():
    user_data = {
        "username": "test2@example.com",
        "password": "12345"
    }
    # Test successful registration
    response = client.post("/auth/login", data=user_data)

    assert response.status_code == 403