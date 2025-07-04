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
async def test_user_register_success():
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "password": "strongpassword123"
    }
    # Test successful registration
    response = client.post("/auth/register", json=user_data)

    assert response.status_code == 201
    response_data = response.json()
    assert response_data is None

@pytest.mark.asyncio
async def test_user_register_failure_by_role():
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "password": "strongpassword123",
        "role": "ADMIN"
    }
    # Test successful registration
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_user_register_failure_by_email_existing():
    user_data = {
        "email": "test@example.com",
        "name": "Daniel",
        "password": "strongpassword123"
    }
    # Test successful registration
    response = client.post("/auth/register", json=user_data)

    assert response.status_code == 409