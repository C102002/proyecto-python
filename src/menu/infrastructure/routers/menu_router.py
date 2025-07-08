from fastapi import APIRouter


menu_router = APIRouter(
    prefix="/menu",
    tags=["Menu"],
)