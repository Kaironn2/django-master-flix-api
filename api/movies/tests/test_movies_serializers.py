from http import HTTPStatus

import pytest

from movies.serializers import MovieSerializer


@pytest.mark.django_db
def test_movies_serializer_valid_data(genre, leonardo_dicaprio, future_date):
    data = {
        'title': 'Titanic',
        'genre': genre.id,
        'release_date': future_date,
        'actors': [leonardo_dicaprio.id],
        'description': 'A love story set on the ill-fated RMS Titanic.',
    }
    serializer = MovieSerializer(data=data)
    assert not serializer.is_valid()
    assert 'release_date' in serializer.errors
    assert (
        'Release date cannot be in the future.'
        in serializer.errors['release_date']
    )


@pytest.mark.django_db
def test_movies_serializer_too_short_description(genre, leonardo_dicaprio):
    EXPECTED_ERROR_MESSAGE = 'Description must be at least 15 characters long.'
    data = {
        'title': 'Titanic',
        'genre': genre.id,
        'release_date': '1997-12-19',
        'actors': [leonardo_dicaprio.id],
        'description': 'Too short',
    }
    serializer = MovieSerializer(data=data)
    assert not serializer.is_valid()
    assert 'description' in serializer.errors
    assert EXPECTED_ERROR_MESSAGE in serializer.errors['description']


@pytest.mark.django_db
def test_movies_serializer_too_long_description(genre, leonardo_dicaprio):
    EXPECTED_ERROR_MESSAGE = 'Description must be at most 500 characters long.'
    long_description = 'A' * 501
    data = {
        'title': 'Titanic',
        'genre': genre.id,
        'release_date': '1997-12-19',
        'actors': [leonardo_dicaprio.id],
        'description': long_description,
    }
    serializer = MovieSerializer(data=data)
    assert not serializer.is_valid()
    assert 'description' in serializer.errors
    assert EXPECTED_ERROR_MESSAGE in serializer.errors['description']


@pytest.mark.django_db
def test_movies_serializer_validation_error(
    api_client, titanic, future_date, v1_movies_url
):
    data = {
        'title': 'Titanic',
        'genre': titanic.genre.id,
        'release_date': future_date,
        'actors': [actor.id for actor in titanic.actors.all()],
        'description': 'A love story set on the ill-fated RMS Titanic.',
    }
    response = api_client.post(v1_movies_url, data, format='json')
    assert response.status_code == HTTPStatus.BAD_REQUEST
