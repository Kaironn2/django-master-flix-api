import json

from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from genres.models import Genre


@csrf_exempt
def genre_create_list_view(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {'message': f'id {new_genre.id} - {new_genre.name}'}, status=201
        )

@csrf_exempt
def genre_detail_view(request: HttpRequest, pk: int) -> JsonResponse:
    genre = get_object_or_404(Genre, pk=pk)

    data = {'id': genre.id, 'name': genre.name}
    return JsonResponse(data)
