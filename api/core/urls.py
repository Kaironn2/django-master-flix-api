from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ap1/v1/', include('actors.urls')),
    path('ap1/v1/', include('genres.urls')),
    path('ap1/v1/', include('movies.urls')),
    path('ap1/v1/', include('reviews.urls')),
]
