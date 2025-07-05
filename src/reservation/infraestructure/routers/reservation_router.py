from fastapi import APIRouter

reservation_router = APIRouter(
    prefix="/reservation",
    tags=["Reservation"],
)