import pytest

from actors.models import Actor, Nationality


@pytest.mark.django_db
def test_actor_str(canada):
    actor = Actor.objects.create(
        name='Johnny Depp', birthday='1963-06-09', nationality=canada,
    )
    assert str(actor) == actor.name


@pytest.mark.django_db
def test_nationality_str():
    country = 'Brazil'
    nationality = Nationality.objects.create(name=country)
    assert str(nationality) == country
