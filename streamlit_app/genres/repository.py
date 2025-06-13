from http import HTTPStatus  # noqa: I001

import requests  # noqa: I001

from core.base_repository import BaseRepository
from .types import GenreDict, GenreCreateDict, MoviesByGenresDict


class GenreRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self._genres_url = self._base_url + 'genres/'
        self._movies_by_genres_url = self._base_url + 'movies/movies-by-genres/'

    def get_genres(self) -> GenreDict:
        response = requests.get(
            url=self._genres_url,
            headers=self._headers,
        )
        return self._handle_response(
            response=response,
            expected_status=HTTPStatus.OK,
            error_message='Get data error',
        )

    def create_genre(self, genre: GenreCreateDict):
        response = requests.post(
            url=self._genres_url,
            headers=self._headers,
            data=genre,
        )
        return self._handle_response(
            response=response,
            expected_status=HTTPStatus.CREATED,
            error_message='Error on creation',
        )

    def get_movies_by_genres(self) -> MoviesByGenresDict:
        response = requests.get(
            url=self._movies_by_genres_url,
            headers=self._headers,
        )
        return self._handle_response(
            response=response,
            expected_status=HTTPStatus.OK,
            error_message='Get data error',
        )
