from http import HTTPStatus  # noqa: I001

import requests  # noqa: I001
import streamlit as st  # noqa: I001

from core.base_repository import BaseRepository
from core.urls import BASE_URL_V1
from .types import GenreDict, GenreCreateDict, MoviesByGenresDict


class GenreRepository(BaseRepository):
    def __init__(self):
        self._genres_url = BASE_URL_V1 + 'genres/'
        self._movies_by_genres_url = BASE_URL_V1 + 'movies/movies-by-genres/'
        self._headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

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
            error_message='Get data error',
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
