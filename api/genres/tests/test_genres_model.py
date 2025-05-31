import pytest

from genres.models import Genre


@pytest.mark.django_db
def test_genre_str():
    genre = Genre.objects.create(name='Action')
    assert str(genre) == genre.name
