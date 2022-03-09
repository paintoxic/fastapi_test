from typing import Optional
from pymongo.database import Database
from packages.web.schemas.movie import MovieAPIModel
from .base import BaseMongoRepository

_COLLECTION_NAME = 'movies'


class MovieMongoRepository(BaseMongoRepository):
    def __init__(self, database: Database) -> None:
        self._collection = database.get_collection(_COLLECTION_NAME)

    def get_by_id(self, id: str):
        movie = self._collection.find_one({"_id": id})
        return movie

    def create(self, item: MovieAPIModel):
        inserted = self._collection.insert_one(self._mapToDal(dict(item)))
        return str(inserted.inserted_id)

    def get_and_count(self, filter: Optional[dict] = None):
        rows = self._collection.find()
        count = self._collection.count_documents({})
        return (rows, count)

    def _mapToDal(self, item: MovieAPIModel):
        return {
            "_id": item["id"],
            "name": item["name"],
            "launch_year": item["launch_year"],
            "director": item["director"],
        }
