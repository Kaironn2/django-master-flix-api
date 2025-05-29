from django.contrib import admin

from actors.models import Actor, Nationality


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality')
    search_fields = ('name',)


@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
