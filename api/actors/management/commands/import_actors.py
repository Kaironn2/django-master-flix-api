import csv
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from actors.models import Actor, Nationality


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Actors csv file name'
        )

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        file_path = settings.BASE_DIR.parent / 'data' / file_name

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            exists_count = 0
            imported_count = 0
            skipped_count = 0

            for row_num, row_data in enumerate(reader, 2):
                name = row_data.get('name')
                birthday = row_data.get('birthday')
                nationality = Nationality.objects.get(name=row_data.get('nationality'))

                if not all([name, birthday, nationality]):
                    self.stdout.write(self.style.NOTICE(
                        f'Row {row_num} dont have all fields.'
                    ))
                    skipped_count += 1
                    continue

                try:
                    birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
                except ValueError:
                    self.stdout.write(self.style.ERROR(f'Invalid date format on row {row_num}'))
                    skipped_count += 1
                    continue

                try:
                    nationality_obj = Nationality.objects.get(name__iexact=nationality)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(
                        f'Row {row_num} nationality doenst exists {nationality} - ERROR: {e}'
                    ))
                    skipped_count += 1
                    continue

                actor, created = Actor.objects.get_or_create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality_obj,
                )

                if not created:
                    self.stdout.write(self.style.NOTICE(f'Actor {name} already exists'))
                    exists_count += 1
                    continue

                self.stdout.write(self.style.WARNING(f'+ Actor {name} created'))
                imported_count += 1

            self.stdout.write(self.style.SUCCESS(
                f'+{imported_count} Actors imported successfully!')
            )
            self.stdout.write(self.style.ERROR(
                f'-{skipped_count} Rows skipped!')
            )
            self.stdout.write(self.style.NOTICE(
                f'-{exists_count} Actors already exists!')
            )
