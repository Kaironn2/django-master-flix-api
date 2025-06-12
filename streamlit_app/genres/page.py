import streamlit as st  # noqa: I001

from core import base_page
from .texts import GenreTexts
from .service import GenreService


class GenrePage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Gêneros'
        self._genre_service = GenreService()

    def render(self):
        st.header(GenreTexts.header)
        st.write(GenreTexts.description)
        self._genre_register()
        self._genres_list()

    def _genres_list(self):
        for genre in self.existing_genres:
            expander = st.expander(genre.title())
            for i in range(1, 10):
                expander.info(f'Filme {i}')

    def _genre_register(self):
        col1, col2 = st.columns([0.5, 0.5])

        with col1:
            genre = st.text_input('Nome do gênero', placeholder='Digite o nome do gênero...')
            normalized_genre = genre.strip().title()

            if st.button('Cadastrar'):
                if not genre:
                    st.error(GenreTexts.error_null_genre, icon='🚨')
                elif normalized_genre in self.existing_genres:
                    st.error(GenreTexts.error_genre_already_exists, icon='🚨')
                else:
                    self._genre_service.create_genre(genre_name=genre)
                    st.success(GenreTexts.sucess_genre_create(genre_name=genre), icon='✅')
                    st.rerun()

    @property
    def existing_genres(self):
        return sorted(self._genre_service.get_genres_names())
