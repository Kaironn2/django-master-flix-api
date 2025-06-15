from typing import List

import streamlit as st

from . import texts
from core import base_page
from core.types import MovieDict, ReviewDict
from movies.service import MovieService
from reviews.service import ReviewService


class ReviewPage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Avaliações'
        self.movie_service = MovieService()
        self.review_service = ReviewService()

    def render(self):
        st.header(texts.header)
        st.write(texts.description)
        self._reviews_list()
        self._review_create_button()

    def _reviews_list(self) -> None:
        self._reviews_subheaders()
        movies_id_title = {movie['id']: movie['title'] for movie in self.movies}
        col1, col2, col3 = st.columns([0.33, 0.33, 0.33])
        for review in self.reviews:
            with col1:
                review_movie = review['movie']
                st.write(movies_id_title[review_movie])
            with col2:
                stars = str(review['stars']) + ' estrela(s)'
                st.write(stars)
            with col3:
                st.write(review['comment'])

    def _reviews_subheaders(self) -> None:
        subheaders = ['Filme', 'Estrelas', 'Comentário']
        columns = st.columns([0.33, 0.33, 0.33])
        for i, col in enumerate(columns):
            with col:
                st.subheader(subheaders[i])

    def _review_create_button(self) -> None:
        if st.button('Adicionar'):
            self._review_create_dialog()

    @st.dialog('Avaliar')
    def _review_create_dialog(self) -> None:
        movies_title_id = {movie['title']: movie['id'] for movie in self.movies}
        selected_movie = st.selectbox('Filme', movies_title_id.keys())

        selected_stars = st.number_input(
            label='Estrelas',
            min_value=1,
            max_value=5,
            step=1
        )

        comment = st.text_input('Comentário [OPCIONAL]')

        if st.button('Avaliar'):
            if not all([selected_stars, selected_movie]):
                st.error('Há campo(s) obrigatório(s) não preenchido(s)')
            else:
                self.review_service.create_review(
                    movie=movies_title_id[selected_movie],
                    stars=selected_stars,
                    comment=comment,
                )
                st.rerun()

    @property
    def movies(self) -> List[MovieDict]:
        return self.movie_service.get_movies()

    @property
    def reviews(self) -> List[ReviewDict]:
        return self.review_service.get_reviews()
