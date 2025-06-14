from http import HTTPStatus

import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_movie_create(
    api_client, genre, leonardo_dicaprio, kate_winslet, v1_movies_url
):
    payload = {
        'title': 'Titanic',
        'release_date': '1997-12-19',
        'genre': genre.id,
        'actors': set([leonardo_dicaprio.id, kate_winslet.id]),
        'description': 'A love story set on the ill-fated RMS Titanic.',
    }
    response = api_client.post(v1_movies_url, payload, format='json')
    assert response.status_code == HTTPStatus.CREATED
    assert Movie.objects.filter(title='Titanic').exists()


@pytest.mark.django_db
def test_retrieve_movie_list(api_client, titanic, v1_movies_url):
    response = api_client.get(v1_movies_url, format='json')
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.data, list)
    assert response.data[0]['title'] == titanic.title


@pytest.mark.django_db
def test_movie_detail_not_found(api_client, v1_movies_detail_url):
    response = api_client.get(v1_movies_detail_url(1), format='json')
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.django_db
def test_retrieve_movie_detail(api_client, titanic, v1_movies_detail_url):
    response = api_client.get(v1_movies_detail_url(titanic.id), format='json')
    assert response.status_code == HTTPStatus.OK
    assert response.data['title'] == titanic.title
    assert len(response.data['actors']) == len(titanic.actors.all())


@pytest.mark.django_db
def test_movie_update(api_client, titanic, v1_movies_detail_url):
    payload = {
        'title': 'Titanic Updated',
        'release_date': '1997-12-19',
        'genre': titanic.genre.id,
        'actors': [actor.id for actor in titanic.actors.all()],
        'description': 'An updated description of the Titanic movie.',
    }
    response = api_client.put(
        v1_movies_detail_url(titanic.id), payload, format='json'
    )
    titanic.refresh_from_db()
    assert response.status_code == HTTPStatus.OK
    assert titanic.title == 'Titanic Updated'


@pytest.mark.django_db
def test_movie_delete(api_client, titanic, v1_movies_detail_url):
    response = api_client.delete(
        v1_movies_detail_url(titanic.id), format='json'
    )
    assert response.status_code == HTTPStatus.NO_CONTENT
    assert not Movie.objects.filter(id=titanic.id).exists()
