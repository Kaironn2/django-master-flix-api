from typing import Any, Optional

import streamlit as st

from core.types import GenreDict, MoviesByGenresDict
from genres.repository import GenreRepository


class GenreService:
    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self) -> GenreDict:
        if 'genres' in st.session_state:
            return st.session_state.genres
        genres = self.genre_repository.get_genres()
        st.session_state.genres = genres
        return genres

    def get_genres_names(self) -> list[str]:
        if 'genres_names' in st.session_state:
            return st.session_state.genres_names
        genres = self.genre_repository.get_genres()
        genres_names = [genre['name'] for genre in genres]
        st.session_state.genres_names = genres_names
        return genres_names

    def create_genre(self, genre_name: str) -> Optional[Any]:
        genre = dict(name=genre_name.title())
        new_genre = self.genre_repository.create_genre(genre=genre)
        st.session_state.genres.append(new_genre)
        return new_genre

    def get_movies_by_genres(self) -> MoviesByGenresDict:
        if 'movies_by_genres' in st.session_state:
            return st.session_state.movies_by_genres
        movies_by_genres = self.genre_repository.get_movies_by_genres()
        st.session_state.movies_by_genres = movies_by_genres
        return movies_by_genres
