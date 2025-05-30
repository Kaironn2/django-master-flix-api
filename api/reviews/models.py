from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='reviews'
    )
    stars = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, 'Avaliação miníma é de 5 estrelas.'),
            MaxValueValidator(5, 'Avaliação máxima é de 5 estrelas.'),
        ]
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.movie.title} - {self.stars} estrelas'

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-id']
