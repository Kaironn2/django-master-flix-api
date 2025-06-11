import streamlit as st  # noqa: I001

from core import base_page
from . import mock, texts


class GenrePage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Gêneros'
        self.existing_genres = sorted({genre['name'].lower() for genre in mock.genres})

    def render(self):
        st.header(texts.header)
        st.write(texts.description)
        self._genres_list()
        self._genre_register()

    def _genres_list(self):
        for genre in self.existing_genres:
            expander = st.expander(genre.title())
            for i in range(1, 10):
                expander.info(f'Teste {i}')

    def _genre_register(self):
        col1, col2 = st.columns([0.5, 0.5])

        with col1:
            genre = st.text_input('Nome do gênero', placeholder='Digite o nome do gênero...')
            normalized_genre = genre.strip().lower()

            if st.button('Cadastrar'):
                if not genre:
                    st.error('Por favor, digite o nome do gênero', icon='🚨')
                elif normalized_genre in self.existing_genres:
                    st.error('Gênero já cadastrado no banco de dados.', icon='🚨')
                else:
                    st.success(f'Gênero {genre} cadastrado com sucesso!', icon='✅')
