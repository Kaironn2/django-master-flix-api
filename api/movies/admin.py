from django.contrib import admin

from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'genre',
        'get_actors',
        'release_date',
        'description',
    )
    search_fields = ('title', 'genre__name', 'actors__name')

    def get_actors(self, obj):  # noqa: PLR6301
        return ', '.join([actor.name for actor in obj.actors.all()])

    get_actors.short_description = 'Atores'
