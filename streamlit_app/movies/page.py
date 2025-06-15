import streamlit as st  # noqa: I001
from typing import List

from core import base_page
from core.types import MovieDict
from .service import MovieService
from . import texts


class MoviePage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Filmes'
        self.movie_service = MovieService()

    def render(self):
        st.header(texts.header)
        st.write(texts.description)
        self._movies_header()
        self._movies_list()

    def _movies_list(self) -> None:
        movies = self.movies

        col1, col2, col3, col4, col5 = st.columns([0.2, 0.2, 0.2, 0.2, 0.2])
        for movie in movies:
            with col1:
                st.write(movie['title'])
            with col2:
                st.write(movie['release_date'])
            with col3:
                st.write(movie['genre']['name'])
            with col4:
                st.write(movie['description'])

    def _movies_header(self) -> None:
        col1, col2, col3, col4, col5 = st.columns([0.2, 0.2, 0.2, 0.2, 0.2])
        with col1:
            st.write('Título')
        with col2:
            st.write('Data de Lançamento')
        with col3:
            st.write('Gênero')
        with col4:
            st.write('Descrição')

    @property
    def movies(self) -> List[MovieDict]:
        return self.movie_service.get_movies()
