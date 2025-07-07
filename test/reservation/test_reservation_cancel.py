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
async def test_reservation_cancel_sucess():
    data = {
        "reservation_id": "197dd255-a202-4aed-b973-bc7af39ee411",
        "client_id": "197dd255-a202-4aed-b973-bc7af39ee411",
    }    
    response = client.post("/reservation/cancel", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data is None
    