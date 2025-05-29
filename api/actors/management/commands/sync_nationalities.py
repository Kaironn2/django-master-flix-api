from django.core.management.base import BaseCommand

from actors.models import Nationality
from actors.services.nationality_service import get_nationalities


class Command(BaseCommand):
    help = 'Sync nationalities from external API'

    def handle(self, *args, **kwargs):
        countries = get_nationalities(charfield_choices=False)

        for country in countries:
            Nationality.objects.get_or_create(name=country)
        self.stdout.write(
            self.style.SUCCESS('Nationalities synced successfully.')
        )
