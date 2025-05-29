from django.contrib import admin
from django.urls import path, include
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('genres.urls')),
    path('', include('actors.urls')),
]
