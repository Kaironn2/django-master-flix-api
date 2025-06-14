from datetime import datetime
from typing import List

import streamlit as st

from core import base_page
from .service import ActorService
from .texts import ActorTexts
from .types import ActorDict, NationalityDict


class ActorPage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Atores'
        self._actor_service = ActorService()

    def render(self):
        st.header(ActorTexts.header)
        st.write(ActorTexts.description)
        self._filters()

    def _actors_list(self, actors: List[ActorDict]) -> None:
        for actor in actors:
            name = actor['name']
            birthday = datetime.strptime(actor['birthday'], '%Y-%m-%d').strftime('%d/%m/%Y')
            nationality = actor['nationality_name']
            st.info(f'{name} - {birthday} - {nationality}')

    def _filters(self):
        actors = self._actor_service.get_actors()
        nationality_map = {n['id']: n['name'] for n in self.nationalities}

        for actor in actors:
            actor['nationality_name'] = nationality_map.get(actor['nationality'], 'Desconhecida')

        col1, col2 = st.columns([0.5, 0.5])

        with col1:
            actor_name = st.text_input('Ator', placeholder='Digite o nome do ator...')
        with col2:
            nationality = st.text_input('Nacionalidade', placeholder='Digite o nome do ator...')

        filtered_actors = [
            actor for actor in actors
            if (actor_name.lower() in actor['name'].lower())
            and (nationality.lower() in actor['nationality_name'].lower())
        ]

        col_btn1, col_btn2, col_btn3 = st.columns([0.1, 0.1, 1.3])
        with col_btn1:
            if st.button('Filtrar'):
                st.rerun()
        with col_btn2:
            self._create_actor_button()

        self._actors_list(actors=filtered_actors)

    def _create_actor_button(self) -> None:
        if st.button('Adicionar'):
            self._create_actor_dialog()

    @st.dialog('Adicionar ator')
    def _create_actor_dialog(self):
        name = st.text_input('Nome do ator', placeholder='Digite o nome do ator...')

        nationality_names = [n['name'] for n in self.nationalities]
        nationality_name = st.selectbox('Nacionalidade', nationality_names)

        birthday = st.date_input(
            'Data de nascimento',
            format='DD/MM/YYYY',
            min_value=datetime(1600, 1, 1),
            max_value=datetime.today()
        )

        if st.button('Confirmar'):
            nationality_id = next(
                (n['id'] for n in self.nationalities if n['name'] == nationality_name), None
            )
            self._actor_service.create_actor(
                name=name,
                birthday=birthday.strftime('%Y-%m-%d'),
                nationality=nationality_id
            )
            st.success(ActorTexts.sucess_actor_created)
            st.rerun()

    @property
    def nationalities(self) -> List[NationalityDict]:
        return self._actor_service.get_nationalities()
