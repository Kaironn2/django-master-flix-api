from datetime import date

from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj: Movie):     # noqa: PLR6301
        reviews = obj.reviews.all()
        if not reviews:
            return None
        return sum(review.stars for review in reviews) / len(reviews)

    def validate_release_date(self, value):     # noqa: PLR6301
        if value > date.today():
            raise serializers.ValidationError(
                'Release date cannot be in the future.'
            )
        return value

    def validate_description(self, value):   # noqa: PLR6301
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
