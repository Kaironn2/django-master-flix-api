from http import HTTPStatus  # noqa: I001
from typing import Any, Dict, Union

import requests

from core.urls import BASE_URL_V1


class Auth:

    def __init__(self):
        self._auth_url = BASE_URL_V1 + 'authentication/token/'

    def get_token(self, username: str, password: str) -> Union[Dict[str, Any]]:
        payload = {
            'username': username,
            'password': password,
        }
        response = requests.post(self._auth_url, payload)

        if response.status_code == HTTPStatus.OK:
            return response.json()
        return {'error': f'Auth error - Status code: {response.status_code}'}
