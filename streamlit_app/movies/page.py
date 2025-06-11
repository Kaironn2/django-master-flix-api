import streamlit as st  # noqa: I001

from core import base_page
from . import texts


class MoviePage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Filmes'

    def render(self):
        st.header(texts.header)
        st.write(texts.description)
