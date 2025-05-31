from unittest.mock import patch

import pytest
from actors.models import Nationality
from django.core.management import call_command

from reviews.models import Review


@pytest.mark.django_db
def test_review_model_str(titanic):
    review = Review.objects.create(
        movie=titanic, stars=5, comment='Great movie!'
    )
    assert str(review) == (f'{titanic.title} - {review.stars} estrelas')


@pytest.mark.django_db
@patch('actors.management.commands.sync_nationalities.get_nationalities')
def test_sync_nationalities_command(mock_get_nationalities):
    mock_get_nationalities.return_value = ['Brazil', 'Canada']

    call_command('sync_nationalities')

    assert Nationality.objects.filter(name='Brazil').exists()
    assert Nationality.objects.filter(name='Canada').exists()
