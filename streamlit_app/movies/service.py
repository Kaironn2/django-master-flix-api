from datetime import datetime
from typing import Any, List, Optional

import streamlit as st

from core.types import MovieDict
from movies.repository import MovieRepository, MovieStatsDict


class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self) -> MovieDict:
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movie_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(
        self,
        title: str,
        actors: List[int],
        genre: int,
        release_date: datetime,
        description: str,
    ) -> Optional[Any]:
        movie = dict(
            title=title,
            actors=actors,
            genre=genre,
            release_date=release_date,
            description=description,
        )
        new_movie = self.movie_repository.create_movie(movie=movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self) -> MovieStatsDict:
        if 'movie_stats' in st.session_state:
            return st.session_state.movie_stats
        movie_stats = self.movie_repository.get_movie_stats()
        st.session_state.movie_stats = movie_stats
        return movie_stats
