from typing import List, TypedDict


class MovieDict(TypedDict):
    id: int
    title: str
    release_date: str
    description: str
    genre: int
    actors: List[int]


class MovieCreateDict(TypedDict):
    title: str
    release_date: str
    description: str
    genre: int
    actors: List[int]
