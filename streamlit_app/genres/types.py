from typing import TypedDict


class GenreDict(TypedDict):
    id: int
    name: str


class GenreCreateDict(TypedDict):
    name: str
