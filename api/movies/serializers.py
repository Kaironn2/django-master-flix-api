from datetime import date  # noqa: I001

from django.db.models import Avg
from rest_framework import serializers

from actors.serializers import ActorSerializer
from genres.models import Genre
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value) -> date:
        if value > date.today():
            raise serializers.ValidationError(
                'Release date cannot be in the future.'
            )
        return value

    def validate_description(self, value) -> str:
        MIN_LENGTH = 15
        MAX_LENGTH = 500

        if len(value) < MIN_LENGTH:
            raise serializers.ValidationError(
                f'Description must be at least {MIN_LENGTH} characters long.'
            )
        if len(value) > MAX_LENGTH:
            raise serializers.ValidationError(
                f'Description must be at most {MAX_LENGTH} characters long.'
            )
        return value


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_rate = serializers.FloatField()


class MovieListDetailSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'genre', 'actors',
            'release_date', 'rate', 'description'
        ]

    def get_rate(self, obj: Movie) -> float:
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return round(rate, 1) if rate else None


class MoviesByGenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['id', 'name', 'movies']
