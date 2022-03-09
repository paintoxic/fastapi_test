from packages.storage.mongo.repositories.base import BaseMongoRepository


class GetById(object):
    def __init__(self, repository: BaseMongoRepository) -> None:
        self._repo = repository

    def execute(self, id: str):        
        return self._repo.get_by_id(id)
