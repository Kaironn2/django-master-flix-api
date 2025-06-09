from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/actors/', include('actors.urls')),
    path('api/v1/authentication/', include('authentication.urls')),
    path('api/v1/genres/', include('genres.urls')),
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/reviews/', include('reviews.urls')),
]
