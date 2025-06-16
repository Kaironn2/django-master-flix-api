import streamlit as st
import plotly.express as px

from . import texts
from core import base_page
from core.types import MovieStatsDict
from movies.service import MovieService


class HomePage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Início'
        self.movie_service = MovieService()

    def render(self):
        st.header(texts.header)
        st.write(texts.description)
        self._cards()
        self._movies_by_genre_chart()

    def _cards(self) -> None:
        total_movies = self.movies_stats['total_movies']
        total_reviews = self.movies_stats['total_reviews']
        average_rate = self.movies_stats['average_rate']

        col1, col2, col3 = st.columns([0.33, 0.33, 0.33])

        with col1.container(height=150):
            st.subheader('🎬 Total de Filmes')
            st.markdown(
                f"<h2 style='text-align:center;'>{total_movies}</h2>",
                unsafe_allow_html=True
            )

        with col2.container(height=150):
            st.subheader('📝 Total de Avaliações')
            st.markdown(
                f"<h2 style='text-align:center;'>{total_reviews}</h2>",
                unsafe_allow_html=True
            )

        with col3.container(height=150):
            st.subheader('⭐ Média de Avaliações')

            filled_stars = int(average_rate)
            star = 0.5
            half_star = (average_rate - filled_stars) >= star
            empty_stars = 5 - filled_stars - int(half_star)

            stars_html = (
                '★' * filled_stars +
                '½' * int(half_star) +
                '☆' * empty_stars
            )

            st.markdown(
                f"<h2 style='text-align:center; color:gold;'>{stars_html}</h2>"
                f"<p style='text-align:center; font-size: 18px;'>{average_rate:.1f}/5</p>",
                unsafe_allow_html=True
            )

    def _movies_by_genre_chart(self) -> None:
        col = st.columns([1])
        with col[0].container(height=420):
            movies_by_genre = self.movies_stats['movies_by_genre']
            if len(movies_by_genre) > 0:
                fig = px.pie(
                    movies_by_genre,
                    values='count',
                    names='genre__name',
                    title='Filmes por Gênero'
                )
                st.plotly_chart(fig)
            else:
                st.write('Sem registros')

    @property
    def movies_stats(self) -> MovieStatsDict:
        return self.movie_service.get_movie_stats()
