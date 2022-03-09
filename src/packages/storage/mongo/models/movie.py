from typing import Optional
from pydantic import BaseModel


class MovieDAL(BaseModel):
    id: Optional[str]
    name: str
    launch_year: int
    director: str

    class Config:
        fields = {'id': '_id'}
