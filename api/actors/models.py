from django.db import models


class Nationality(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Nacionalidade'
        verbose_name_plural = 'Nacionalidades'


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.ForeignKey(
        Nationality, on_delete=models.PROTECT, related_name='actors'
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name', 'birthday', 'nationality']
        ordering = ['name']
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'
