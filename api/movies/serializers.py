from datetime import date

from django.db.models import Avg
from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj: Movie):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return round(rate, 1) if rate else None

    def validate_release_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                'Release date cannot be in the future.'
            )
        return value

    def validate_description(self, value):
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
