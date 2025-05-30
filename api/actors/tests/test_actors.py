from http import HTTPStatus

import pytest

from actors.models import Actor


@pytest.mark.django_db
def test_actor_create(api_client, canada):
    payload = {
        'name': 'Johnny Depp',
        'birthday': '1963-06-09',
        'nationality': canada.name,
    }
    response = api_client.post('/actors/', payload, format='json')
    assert response.status_code == HTTPStatus.CREATED
    assert Actor.objects.filter(name='Johnny Depp').exists()


@pytest.mark.django_db
def test_retrieve_actor_list(api_client):
    response = api_client.get('/actors/', format='json')
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_actor_detail_not_found(api_client):
    response = api_client.get('/actors/1/', format='json')
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.django_db
def test_retrieve_actor_detail(api_client, actor):
    response = api_client.get(f'/actors/{actor.id}/', format='json')
    assert response.status_code == HTTPStatus.OK
    assert response.data['name'] == 'Johnny Depp'


@pytest.mark.django_db
def test_actor_update(api_client, actor):
    payload = {
        'name': 'Johnny Depp Updated',
        'birthday': '1963-06-09',
        'nationality': actor.nationality.name,
    }
    response = api_client.put(f'/actors/{actor.id}/', payload, format='json')
    actor.refresh_from_db()
    assert response.status_code == HTTPStatus.OK
    assert actor.name == 'Johnny Depp Updated'


@pytest.mark.django_db
def test_actor_delete(api_client, actor):
    response = api_client.delete(f'/actors/{actor.id}/', format='json')
    assert response.status_code == HTTPStatus.NO_CONTENT
    assert not Actor.objects.filter(id=actor.id).exists()
