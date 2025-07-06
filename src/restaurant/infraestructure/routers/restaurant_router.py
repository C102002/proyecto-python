from fastapi import APIRouter


restaurant_router = APIRouter(
    prefix="/restaurant",
    tags=["Restaurant"],
)