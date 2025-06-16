from datetime import datetime
import json
from typing import Any, List, Optional

from core.types import MovieDict
from movies.repository import MovieRepository, MovieStatsDict


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
        print(json.dumps(movie, indent=2, ensure_ascii=False, default=str))
        return self.movie_repository.create_movie(movie=movie)

    def get_movie_stats(self) -> MovieStatsDict:
        return self.movie_repository.get_movie_stats()
