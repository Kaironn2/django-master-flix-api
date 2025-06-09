from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from actors.models import Actor, Nationality
from actors.serializers import ActorSerializer, NationalitySerializer


class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class NationalityListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class NationalityRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = (IsAuthenticated,)
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
