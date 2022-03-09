from pydantic import BaseModel
from typing import Optional

def MovieAPI(item) -> dict:
    return {
        "id": item["_id"],
        "name": item["name"],
        "launch_year": item["launch_year"],
        "director": item["director"],
    }


def Movies(items) -> list:
    return [MovieAPI(item) for item in items]


class MovieAPIModel(BaseModel):
    id: Optional[str]
    name: str
    launch_year: int
    director: str
