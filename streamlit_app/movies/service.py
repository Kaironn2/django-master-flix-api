from datetime import datetime
from typing import Any, List, Optional

from core.types import MovieDict
from movies.repository import MovieRepository


class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self) -> MovieDict:
        return self.movie_repository.get_movies()

    def create_movie(
        self,
        title: str,
        actors: List[int],
        genre: int,
        release_date: datetime,
        description: str,
    ) -> Optional[Any]:
        movie = dict(
            title=title,
            actors=actors,
            genre=genre,
            release_date=release_date,
            description=description,
        )
        return self.movie_repository.create_movie(movie=movie)
