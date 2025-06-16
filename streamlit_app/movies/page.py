from datetime import datetime
from typing import List

import streamlit as st  # noqa: I001

from actors.service import ActorService
from genres.service import GenreService
from core import base_page
from core.types import ActorDict, GenreDict, MovieDict
from .service import MovieService
from . import texts


class MoviePage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Filmes'
        self.actor_service = ActorService()
        self.genre_service = GenreService()
        self.movie_service = MovieService()

    def render(self):
        st.header(texts.header)
        st.write(texts.description)
        self._create_movies_button()
        with st.container(border=True):
            self._movies_list(self.movies)

    def _movies_list(self, filtered_movies: MovieDict) -> None:
        self._movies_header()
        col1, col2, col3, col4, col5 = st.columns([0.2, 0.2, 0.2, 0.2, 0.2])
        for movie in filtered_movies:
            with col1:
                st.write(movie['title'])
            with col2:
                st.write(
                    datetime.strptime(movie['release_date'], '%Y-%m-%d').strftime('%d/%m/%Y')
                )
            with col3:
                st.write(movie['genre']['name'])
            with col4:
                st.write(str(movie['rate'])) if movie['rate'] else st.write('Sem avaliações')
            with col5:
                st.write(movie['description'])

    def _movies_header(self) -> None:
        subheaders = [
            'Título', 'Data de Lançamento', 'Gênero', 'Avaliação', 'Descrição'
        ]
        columns = st.columns([0.2, 0.2, 0.2, 0.2, 0.2])
        for i, col in enumerate(columns):
            with col:
                st.subheader(subheaders[i])

    def _create_movies_button(self) -> None:
        if st.button('Adicionar'):
            self._create_movie_dialog()

    @st.dialog('Adicionar filme')
    def _create_movie_dialog(self) -> None:
        actor_names = {actor['name']: actor['id'] for actor in self.actors}
        genre_names = {actor['name']: actor['id'] for actor in self.genres}

        title = st.text_input('Título do filme')
        selected_genre = st.selectbox('Gênero', genre_names.keys())
        description = st.text_input('Descrição')
        release_date = st.date_input(
            'Data de lançamento',
            format='DD/MM/YYYY',
            min_value=datetime(1600, 1, 1),
            max_value=datetime.today()
        )
        selected_actors = st.multiselect('Atores', actor_names.keys())

        actors_ids = [actor_names[name] for name in selected_actors]
        genre_id = genre_names[selected_genre]

        if st.button('Confirmar'):
            if not all([title, release_date, selected_actors]):
                st.error('Preencha todos os campos obrigatórios')
            else:
                self.movie_service.create_movie(
                    title=title,
                    genre=genre_id,
                    description=description,
                    release_date=release_date,
                    actors=actors_ids,
                )
                st.rerun()
                st.success('Ator salvo com sucesso!')

    @property
    def actors(self) -> List[ActorDict]:
        return self.actor_service.get_actors()

    @property
    def genres(self) -> List[GenreDict]:
        return self.genre_service.get_genres()

    @property
    def movies(self) -> List[MovieDict]:
        return self.movie_service.get_movies()
