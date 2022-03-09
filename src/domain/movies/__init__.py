from os import getenv
from .use_cases.get_by_id import GetById
from .use_cases.create_one import CreateOne
from .use_cases.get_and_count import GetAndCount
from packages.storage.mongo.repositories.movie_repo import MovieMongoRepository
from packages.storage.mongo import CONNECTIONS

_CONNECTION_KEY = getenv("DB_CONNECTION_KEY", 'my-app')
_DB_NAME = getenv("DB_NAME", 'database')

_CLIENT = CONNECTIONS.get(_CONNECTION_KEY)

_DATABASE = _CLIENT.get_database(_DB_NAME)

get_by_id = GetById(MovieMongoRepository(_DATABASE)).execute
create_one = CreateOne(MovieMongoRepository(_DATABASE)).execute
get_and_count = GetAndCount(MovieMongoRepository(_DATABASE)).execute
