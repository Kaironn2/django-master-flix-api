from core.base_repository import BaseRepository
from .types import GenreDict, GenreCreateDict, MoviesByGenresDict


class GenreRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self._genres_url = self._base_url + 'genres/'
        self._movies_by_genres_url = self._base_url + 'movies/movies-by-genres/'

    def get_genres(self) -> GenreDict:
        return self._handle_retrieve(url=self._genres_url)

    def create_genre(self, genre: GenreCreateDict):
        return self._handle_create(
            url=self._genres_url,
            data=genre,
        )

    def get_movies_by_genres(self) -> MoviesByGenresDict:
        return self._handle_retrieve(url=self._movies_by_genres_url)
