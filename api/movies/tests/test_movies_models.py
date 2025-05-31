import pytest
from django.contrib import admin

from movies.admin import MovieAdmin
from movies.models import Movie


@pytest.mark.django_db
def test_movie_str(titanic):
    assert str(titanic) == titanic.title


@pytest.mark.django_db
def test_movie_admin_get_actors(titanic):
    admin_inst = MovieAdmin(Movie, admin.site)
    expected = ', '.join(actor.name for actor in titanic.actors.all())
    result = admin_inst.get_actors(titanic)
    assert result == expected
