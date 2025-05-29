from django.urls import path

from actors.views import (
    ActorListCreateView,
    ActorRetrieveUpdateDestroyView,
    NationalityListCreateView,
    NationalityRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('actors/', ActorListCreateView.as_view(), name='actor-list-create'),
    path(
        'actors/<int:pk>/',
        ActorRetrieveUpdateDestroyView.as_view(),
        name='actor-detail',
    ),
    path(
        'nationalities/',
        NationalityListCreateView.as_view(),
        name='nationality-list-create',
    ),
    path(
        'nationalities/<int:pk>/',
        NationalityRetrieveUpdateDestroyView.as_view(),
        name='nationality-detail',
    ),
]
