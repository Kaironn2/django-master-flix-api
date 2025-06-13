from datetime import datetime
from typing import List

import streamlit as st  # noqa: I001

from core import base_page
from .service import ActorService
from .texts import ActorTexts
from .types import NationalityDict


class ActorPage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Atores'
        self._actor_service = ActorService()

    def render(self):
        st.header(ActorTexts.header)
        st.write(ActorTexts.description)
        self._actors_list()

    def _actors_list(self) -> None:
        for actor in self._actor_service.get_actors():
            id = actor['id']
            name = actor['name']
            birthday = datetime.strptime(actor['birthday'], '%Y-%m-%d').strftime('%d/%m/%Y')
            nationality = next(
                (n['name'] for n in self.nationalities_list if n['id'] == actor['nationality']),
                'Desconhecida'
            )
            st.info(f'{id} - {name} - {birthday} - {nationality}')

    @property
    def nationalities_list(self) -> List[NationalityDict]:
        return self._actor_service.get_nationalities()
