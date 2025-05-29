from rest_framework import generics

from actors.models import Actor, Nationality
from actors.serializers import ActorSerializer, NationalitySerializer


class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class NationalityListCreateView(generics.ListCreateAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class NationalityRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
