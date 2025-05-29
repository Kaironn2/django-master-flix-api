from rest_framework import serializers

from actors.models import Actor, Nationality


class ActorSerializer(serializers.ModelSerializer):
    nationality = serializers.SlugRelatedField(
        queryset=Nationality.objects.all(), slug_field='name'
    )

    class Meta:
        model = Actor
        fields = '__all__'


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'
