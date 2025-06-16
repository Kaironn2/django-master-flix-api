from typing import Any, List, Optional

from core.base_repository import BaseRepository
from core.types import MovieCreateDict, MovieDict, MovieStatsDict


class MovieRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self._movies_url = self._base_url + 'movies/'
        self._movies_stats_url = self._movies_url + 'stats/'

    def get_movies(self) -> List[MovieDict]:
        return self._handle_retrieve(url=self._movies_url)

    def create_movie(self, movie: MovieCreateDict) -> Optional[Any]:
        return self._handle_create(
            url=self._movies_url,
            data=movie,
        )

    def get_movie_stats(self) -> MovieStatsDict:
        return self._handle_retrieve(url=self._movies_stats_url)
