from fastapi import HTTPException
from packages.storage.mongo.models.movie import MovieDAL
from packages.storage.mongo.repositories.base import BaseMongoRepository


class CreateOne(object):
    def __init__(self, repository: BaseMongoRepository) -> None:
        self._repo = repository

    def execute(self, item: MovieDAL):
        _, count = self._repo.get_and_count({"name": item['name']})
        if count > 0:
            raise HTTPException(status_code=400, detail="Movie already exist")
        return self._repo.create(item)
