from typing import List, TypedDict


class GenreDict(TypedDict):
    id: int
    name: str


class GenreCreateDict(TypedDict):
    name: str


class MovieDict(TypedDict):
    id: int
    title: str
    release_date: str
    description: str
    genre: int
    actors: List[int]


class MoviesByGenresDict(TypedDict):
    id: int
    name: str
    movies: List[MovieDict]
