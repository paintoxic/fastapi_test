from fastapi import APIRouter
from .movies import movies_router

api_v1 = APIRouter()

api_v1.include_router(movies_router)
