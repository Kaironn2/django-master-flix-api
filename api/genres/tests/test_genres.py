from http import HTTPStatus

import pytest

from genres.models import Genre


@pytest.mark.django_db
def test_genre_create(api_client):
    payload = {'name': 'action'}
    response = api_client.post('/api/v1/genres/', payload, format='json')
    assert response.status_code == HTTPStatus.CREATED
    assert Genre.objects.filter(name='action').exists()


@pytest.mark.django_db
def test_retrieve_genre_list(api_client, action_genre):
    response = api_client.get('/api/v1/genres/', format='json')
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.data, list)
    assert response.data[0]['name'] == action_genre.name


@pytest.mark.django_db
def test_genre_detail_not_found(api_client):
    response = api_client.get('/api/v1/genres/1/', format='json')
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.django_db
def test_retrieve_genre_detail(api_client, action_genre):
    response = api_client.get(
        f'/api/v1/genres/{action_genre.id}/', format='json'
    )
    assert response.status_code == HTTPStatus.OK
    assert response.data['name'] == action_genre.name


@pytest.mark.django_db
def test_genre_update(api_client, action_genre):
    payload = {'name': 'action updated'}
    response = api_client.put(
        f'/api/v1/genres/{action_genre.id}/', payload, format='json'
    )
    action_genre.refresh_from_db()
    assert response.status_code == HTTPStatus.OK
    assert action_genre.name == 'action updated'


@pytest.mark.django_db
def test_genre_delete(api_client, action_genre):
    response = api_client.delete(
        f'/api/v1/genres/{action_genre.id}/', format='json'
    )
    assert response.status_code == HTTPStatus.NO_CONTENT
    assert not Genre.objects.filter(id=action_genre.id).exists()
