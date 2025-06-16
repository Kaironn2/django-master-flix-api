from datetime import datetime
from typing import List, Literal, TypedDict


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
    rate: float | None

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


class ReviewCreateDict(TypedDict):
    movie: int
    stars: int
    comment: str


class ReviewDict(ReviewCreateDict):
    id: int


class MovieStatsDict(TypedDict):
    total_movies = int
    movies_by_genre = List[int]
    total_reviews = int
    average_rate = float
