from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView
from actors.views import (
    ActorListCreateView, ActorRetrieveUpdateDestroyView,
    NationalityListCreateView, NationalityRetrieveUpdateDestroyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreListCreateView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
    path('actors/', ActorListCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail'),
    path('nationalities/', NationalityListCreateView.as_view(), name='nationality-create-list'),
    path('nationalities/<int:pk>/', NationalityRetrieveUpdateDestroyView.as_view(), name='nationality-detail'),
]
