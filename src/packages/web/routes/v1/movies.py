from fastapi import APIRouter

from packages.web.schemas.movie import MovieAPIModel
from ...controllers import movies_controller

movies_router = APIRouter()


@movies_router.get('/get-one/{id}', tags=["movies"])
async def get_by_id(id):
    return movies_controller.get_by_id(id)


@movies_router.get('/get-all', tags=["movies"])
async def get_all():
    return movies_controller.get_all()


@movies_router.post('/create-one', tags=["movies"])
async def create_one(movie: MovieAPIModel):
    return movies_controller.create(movie)
