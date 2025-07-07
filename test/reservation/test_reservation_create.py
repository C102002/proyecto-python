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
async def test_reservation_create_sucess():
    data = {
        "date_start": "00:46:53.358Z",
        "date_end": "02:46:53.358Z",
        "client_id": "197dd255-a202-4aed-b973-bc7af39ee411",
        "reservation_date": "2025-07-07",
        "table_number_id": "4ac95fe2-2879-445c-b3a1-bb136be2ab2a",
        "restaurant_id": "4ac95fe2-2879-445c-b3a1-bb136be2ab2a",
        "dish_id": [
            "4ac95fe2-2879-445c-b3a1-bb136be2ab2a"
        ]
    }    
    # Test successful registration
    response = client.post("/reservation/create", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data is None
    
@pytest.mark.asyncio
async def test_create_fail_reservation_time_more_than_4hours():
    data = {
        "date_start": "00:46:53.358Z",
        "date_end": "08:46:53.358Z",
        "client_id": "197dd255-a202-4aed-b973-bc7af39ee411",
        "reservation_date": "2025-07-07",
        "table_number_id": "4ac95fe2-2879-445c-b3a1-bb136be2ab2a",
        "restaurant_id": "4ac95fe2-2879-445c-b3a1-bb136be2ab2a",
        "dish_id": [
            "4ac95fe2-2879-445c-b3a1-bb136be2ab2a"
        ]
    }    
    response = client.post("/reservation/create", json=data)
    assert response.status_code == 500
    response_data = response.json()
    assert response_data is None
    