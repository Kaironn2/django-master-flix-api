from django.urls import path

from reviews.views import (
    ReviewListCreateView,
    ReviewRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list-create'),
    path('<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),
]
