from fastapi.testclient import TestClient
from src.main import app
import pytest
from dotenv import load_dotenv
import asyncio
import platform

load_dotenv()

client = TestClient(app)

@pytest.mark.order(1)
@pytest.mark.asyncio
async def test_user_register_success():
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "password": "strongpassword123"
    }
    # Test successful registration
    response = client.post("/auth/register", json=user_data)
    
    print("STATUS:", response.status_code)
    print("BODY  :", response.text)

    assert response.status_code == 201
    response_data = response.json()
    assert response_data is None

@pytest.mark.order(2)
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

@pytest.mark.order(3)
@pytest.mark.asyncio
async def test_user_register_failure_by_email_existing():
    user_data = {
        "email": "test@example.com",
        "name": "Daniel",
        "password": "strongpassword123"
    }

    # Test successful registration
    response = client.post("/auth/register", json=user_data)
    
    print("STATUS:", response.status_code)
    print("BODY  :", response.text)

    assert response.status_code == 409