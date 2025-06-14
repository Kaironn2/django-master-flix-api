from abc import ABC
from http import HTTPStatus
from typing import Any, Dict, Optional

import requests
import streamlit as st

from .urls import BASE_URL_V1
from login.service import logout


class BaseRepository:
    def __init__(self):
        super().__init__()
        self._base_url = BASE_URL_V1
        self._headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def _handle_retrieve(
            self, url: str, expected_status: HTTPStatus = HTTPStatus.OK, 
            error_message: str = 'Get data error'
    ) -> Optional[Any]:
        response = requests.get(
            url=url,
            headers=self._headers,
        )
        if response.status_code == expected_status:
            return response.json()
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            logout()
            return None
        raise Exception({'error': f'{error_message} - Status code: {response.status_code}'})

    def _handle_create(
            self, url: str, data: Dict[str, Any],
            expected_status: HTTPStatus = HTTPStatus.CREATED, 
            error_message: str = 'Get data error'
    ) -> Optional[Any]:
        response = requests.get(
            url=url,
            headers=self._headers,
            data=data
        )
        if response.status_code == expected_status:
            return response.json()
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            logout()
            return None
        raise Exception({'error': f'{error_message} - Status code: {response.status_code}'})
