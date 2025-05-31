from datetime import date, timedelta

import pytest
from actors.models import Actor, Nationality
from genres.models import Genre
from rest_framework.test import APIClient

from movies.models import Movie


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def future_date():
    return (date.today() + timedelta(days=30)).isoformat()


@pytest.fixture
def v1_movies_url():
    return '/api/v1/movies/'


@pytest.fixture
def v1_movies_detail_url():
    def _url(movie_id):
        return f'/api/v1/movies/{movie_id}/'
    return _url


@pytest.fixture
def united_states():
    return Nationality.objects.create(name='United States')


@pytest.fixture
def united_kingdom():
    return Nationality.objects.create(name='United Kingdom')


@pytest.fixture
def leonardo_dicaprio(united_states):
    return Actor.objects.create(
        name='Leonardo DiCaprio',
        birthday='1974-11-11',
        nationality=united_states,
    )


@pytest.fixture
def kate_winslet(united_kingdom):
    return Actor.objects.create(
        name='Kate Winslet',
        birthday='1975-10-05',
        nationality=united_kingdom,
    )


@pytest.fixture
def genre():
    return Genre.objects.create(name='Drama')


@pytest.fixture
def titanic(genre, leonardo_dicaprio, kate_winslet):
    movie = Movie.objects.create(
        title='Titanic',
        release_date='1997-12-19',
        genre=genre,
        description='A love story set on the ill-fated RMS Titanic.',
    )
    movie.actors.set([leonardo_dicaprio, kate_winslet])
    return movie
