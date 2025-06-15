from datetime import datetime
from typing import List, TypedDict


class GenreCreateDict(TypedDict):
    name: str


class GenreDict(GenreCreateDict):
    id: int


class MovieCreateDict(TypedDict):
    title: str
    release_date: str
    description: str
    genre: GenreDict
    actors: List[int]

class MovieDict(MovieCreateDict):
    id: int


class MoviesByGenresDict(TypedDict):
    id: int
    name: str
    movies: List[MovieDict]


class ActorCreateDict(TypedDict):
    birthday: datetime
    nationality: int


class ActorDict(TypedDict):
    id: int


class NationalityDict(TypedDict):
    id: int
    name: str
