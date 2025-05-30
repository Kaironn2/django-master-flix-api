import pytest
from rest_framework.test import APIClient

from actors.models import Actor, Nationality


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def canada():
    return Nationality.objects.create(name='canada')


@pytest.fixture
def actor(canada):
    return Actor.objects.create(
        name='Johnny Depp', birthday='1963-06-09', nationality=canada
    )
