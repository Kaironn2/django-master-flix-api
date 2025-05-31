from http import HTTPStatus

import pytest

from reviews.models import Review


@pytest.mark.django_db
def test_review_create(api_client, titanic):
    payload = {
        'movie': titanic.id,
        'stars': 5,
        'comment': 'An epic love story with stunning visuals.',
    }
    response = api_client.post('/api/v1/reviews/', payload, format='json')
    assert response.status_code == HTTPStatus.CREATED
    assert Review.objects.filter(movie=titanic).exists()


@pytest.mark.django_db
def test_retrieve_review_list(api_client, review):
    response = api_client.get('/api/v1/reviews/', format='json')
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.data, list)
    assert response.data[0]['movie'] == review.movie.id
    assert response.data[0]['stars'] == review.stars
    assert response.data[0]['comment'] == review.comment


@pytest.mark.django_db
def test_review_detail_not_found(api_client):
    response = api_client.get('/api/v1/reviews/1/', format='json')
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.django_db
def test_retrieve_review_detail(api_client, review):
    response = api_client.get(f'/api/v1/reviews/{review.id}/', format='json')
    assert response.status_code == HTTPStatus.OK
    assert response.data['movie'] == review.movie.id
    assert response.data['stars'] == review.stars
    assert response.data['comment'] == review.comment


@pytest.mark.django_db
def test_review_update(api_client, review):
    stars = 4
    payload = {
        'movie': review.movie.id,
        'stars': stars,
        'comment': 'An updated comment for the review.',
    }
    response = api_client.put(
        f'/api/v1/reviews/{review.id}/', payload, format='json'
    )
    review.refresh_from_db()
    assert response.status_code == HTTPStatus.OK
    assert review.stars == stars
    assert review.comment == 'An updated comment for the review.'


@pytest.mark.django_db
def test_review_delete(api_client, review):
    response = api_client.delete(
        f'/api/v1/reviews/{review.id}/', format='json'
    )
    assert response.status_code == HTTPStatus.NO_CONTENT
    assert not Review.objects.filter(id=review.id).exists()
