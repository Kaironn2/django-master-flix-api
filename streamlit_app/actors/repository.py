from http import HTTPStatus
from typing import Any, List, Optional

import requests

from .types import ActorDict, NationalityDict
from core.base_repository import BaseRepository


class ActorRepository(BaseRepository):

    def __init__(self):
        super().__init__()
        self._actors_url = self._base_url + 'actors/'
        self._nationalities_url = self._actors_url + 'nationalities/'

    def get_actors(self) -> List[ActorDict]:
        response = requests.get(
            url=self._actors_url,
            headers=self._headers,
        )
        return self._handle_response(
            response=response,
            expected_status=HTTPStatus.OK,
            error_message='Get data error'
        )

    def create_actor(self, actor: ActorDict) -> Optional[Any]:
        response = requests.post(
            url=self._actors_url,
            headers=self._headers,
            data=actor
        )
        return self._handle_response(
            response=response,
            expected_status=HTTPStatus.CREATED,
            error_message='Error on creation'
        )

    def get_nationalities(self) -> List[NationalityDict]:
        response = requests.get(
            url=self._nationalities_url,
            headers=self._headers,
        )
        return self._handle_response(
            response=response,
            expected_status=HTTPStatus.OK,
            error_message='Get data error'
        )
