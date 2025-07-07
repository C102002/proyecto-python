# # tests/test_restaurant_create.py

# from httpx import AsyncClient
# import pytest
# from fastapi.testclient import TestClient
# from dotenv import load_dotenv
# import asyncio
# import platform
# import uuid

# from src.main import app

# # On Windows, tell asyncio to use the SelectorEventLoop
# if platform.system() == "Windows":
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# load_dotenv()
# client = TestClient(app)

# # TODO terminar de acomodarlo porque da error de un hilo de sesion de la bd
# @pytest.mark.asyncio
# async def test_create_restaurant_success():
#     """
#     GIVEN a valid payload for creating a restaurant
#     WHEN POST /restaurant is called
#     THEN it returns 201 and a body containing the new restaurant data
#     """
    
#     payload={
#     "closing_time": "22:00:00",
#     "lat": -0.180653,
#     "lng": -78.467834,
#     "name": "Mi Restaurante",
#     "opening_time": "09:00:00"
#     }
    
#     response = client.post("/restaurant", json=payload)
    
#     print("STATUS:", response.status_code)
#     print("BODY  :", response.text)

    
#     assert response.status_code == 201

#     data = response.json()
#     # Verify that the response contains all expected fields
#     assert "id" in data
#     assert uuid.UUID(data["id"])  # valid UUID
#     assert data["name"] == payload["name"]
#     assert data["lat"] == pytest.approx(payload["lat"], rel=1e-6)
#     assert data["lng"] == pytest.approx(payload["lng"], rel=1e-6)
#     assert data["opening_time"] == payload["opening_time"]
#     assert data["closing_time"] == payload["closing_time"]


# @pytest.mark.asyncio
# async def test_create_restaurant_missing_field():
#     """
#     GIVEN an invalid payload missing the 'name' field
#     WHEN POST /restaurant is called
#     THEN it returns 422 Unprocessable Entity with a validation error
#     """
#     payload = {
#         "lat": -0.180653,
#         "lng": -78.467834,
#         "opening_time": "08:00",
#         "closing_time": "22:00"
#     }

#     response = client.post("/restaurant", json=payload)
#     assert response.status_code == 422

#     data = response.json()
#     # FastAPI returns a list of validation errors under 'detail'
#     assert "detail" in data
#     assert any(err["loc"][-1] == "name" for err in data["detail"])


# @pytest.mark.asyncio
# async def test_create_restaurant_invalid_times():
#     """
#     GIVEN a payload where closing_time is before opening_time
#     WHEN POST /restaurant is called
#     THEN it returns 400 Bad Request with a business validation error
#     """
#     payload = {
#         "name": "Night Owl Lounge",
#         "lat": -0.180653,
#         "lng": -78.467834,
#         "opening_time": "22:00",
#         "closing_time": "06:00"  # invalid: before opening
#     }

#     response = client.post("/restaurant", json=payload)
#     assert response.status_code == 400

#     data = response.json()
#     assert "detail" in data
#     # Depending on implementation, you might check specific error message
#     assert "invalid restaurant" in data["detail"].lower() \
#         and "opening time" in data["detail"].lower() \
#         and "closing time" in data["detail"].lower()
