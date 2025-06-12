from abc import ABC
from http import HTTPStatus
from typing import Optional, Any

import requests

from login.service import logout


class BaseRepository:
    def _handle_response(
            self, response: requests.Response, 
            expected_status: HTTPStatus | int, error_message: str = 'Unexpected Error'
    ) -> Optional[Any]:
        if response.status_code == expected_status:
            return response.json()
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            logout()
            return None
        raise Exception({'error': f'{error_message} - Status code: {response.status_code}'})
