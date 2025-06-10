from django.urls import path

from actors.views import (
    ActorListCreateView,
    ActorRetrieveUpdateDestroyView,
    NationalityListCreateView,
    NationalityRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', ActorListCreateView.as_view(), name='actor-list-create'),
    path('<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail',),
    path('nationalities/', NationalityListCreateView.as_view(), name='nationality-list-create',),
    path('nationalities/<int:pk>/', NationalityRetrieveUpdateDestroyView.as_view(), name='nationality-detail'),  # noqa: E501
]
