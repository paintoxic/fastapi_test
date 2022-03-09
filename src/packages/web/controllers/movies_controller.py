from fastapi import HTTPException
import domain.movies as movies_svc
from packages.helpers.uuid import generate_uuid4, is_valid_uuid_4
from packages.storage.mongo.models.movie import MovieDAL
from packages.web.schemas.movie import MovieAPI, MovieAPIModel, Movies


class MovieController(object):
    def __init__(self):
        pass

    def get_by_id(self, id: str):
        result = movies_svc.get_by_id(id)
        return MovieAPI(result)

    def get_all(self):
        rows, count = movies_svc.get_and_count()
        return {"rows": Movies(rows), "count": count}

    def create(self, movie: MovieAPIModel):
        entity = self._add_id(movie)
        result = movies_svc.create_one(entity)
        return {"id": result}

    def _add_id(self, item: MovieAPIModel) -> MovieDAL:
        movie = dict(item)
        if movie["id"] is None:
            movie["id"] = generate_uuid4()
        elif is_valid_uuid_4(movie["id"]) is False:
            raise HTTPException(status_code=400, detail="Id is not valid")
        return movie

    def _mapToApi(self, item: MovieDAL) -> dict:
        return MovieAPI(item)
