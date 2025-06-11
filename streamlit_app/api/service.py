from http import HTTPStatus
from typing import Any, Dict, Union

import requests


class Auth:

    def __init__(self):
        self._base_url = 'http://127.0.0.1:8000/api/v1/'
        self._auth_url = f'{self._base_url}authentication/token/'

    def get_token(self, username: str, password: str) -> Union[Dict[str, Any]]:
        payload = {
            'username': username,
            'password': password,
        }
        response = requests.post(self._auth_url, payload)

        if response.status_code == HTTPStatus.OK:
            return response.json()
        return {'error': f'Auth error - Status code: {response.status_code}'}
