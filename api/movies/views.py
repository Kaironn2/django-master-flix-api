from http import HTTPStatus

from django.db.models import Avg, Count
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from reviews.models import Review

from movies.models import Movie
from movies.serializers import MovieListDetailSerializer, MovieSerializer, MovieStatsSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()

    def get(self, request: Request) -> Response:
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_rate = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        average_rate = round(average_rate, 1) if average_rate else 0

        data = {
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'average_rate': average_rate,
            }

        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return Response(
            data=serializer.validated_data,
            status=HTTPStatus.OK,
        )
