from actors.models import Actor
from django.db import models
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='movies'
    )
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['release_date']
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
