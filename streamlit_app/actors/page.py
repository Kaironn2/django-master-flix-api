import streamlit as st  # noqa: I001

from core import base_page
from . import texts


class ActorPage(base_page.Page):
    def __init__(self):
        super().__init__()
        self.title = 'Atores'

    def render(self):
        st.header(texts.header)
        st.write(texts.description)
