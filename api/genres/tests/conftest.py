import pytest
from rest_framework.test import APIClient

from genres.models import Genre


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def action_genre():
    return Genre.objects.create(name='action')
