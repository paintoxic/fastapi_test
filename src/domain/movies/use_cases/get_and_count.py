from typing import Optional
from packages.storage.mongo.repositories.base import BaseMongoRepository


class GetAndCount(object):
    def __init__(self, repository: BaseMongoRepository) -> None:
        self._repo = repository

    def execute(self, filter: Optional[dict] = None):
        return self._repo.get_and_count(filter)
