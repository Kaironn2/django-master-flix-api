from datetime import datetime
from typing import TypedDict


class ActorDict(TypedDict):
    id: int
    name: str
    birthday: datetime
    nationality: int


class NationalityDict(TypedDict):
    id: int
    name: str
