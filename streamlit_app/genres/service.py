from typing import Any, Optional

from genres.repository import GenreRepository

from .types import GenreDict, MoviesByGenresDict


class GenreService:
    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self) -> GenreDict:
        return self.genre_repository.get_genres()

    def get_genres_names(self) -> list[str]:
        genres = self.genre_repository.get_genres()
        return [genre['name'] for genre in genres]

    def create_genre(self, genre_name: str) -> Optional[Any]:
        genre = {'name': genre_name.title()}
        return self.genre_repository.create_genre(genre=genre)

    def get_movies_by_genres(self) -> MoviesByGenresDict:
        return self.genre_repository.get_movies_by_genres()
