import streamlit as st
from core import base_page

from . import texts
from .service import login


class LoginPage(base_page.Page):

    def __init__(self):
        super().__init__()
        self.title = 'Login'

    def render(self):
        self._center_align()

        col1, col2, col3 = st.columns([0.33, 0.33, 0.33])
        with col2:
            st.header(texts.header)
            st.write(texts.description)
            self._user_inputs()
            self._login_button()

    def _user_inputs(self):
        self.username = st.text_input('Usuário', placeholder='Digite seu usuário')
        self.password = st.text_input('Senha', type='password', placeholder='Digite sua senha')

    def _login_button(self):
        if st.button('Login'):
            login(
                username=self.username,
                password=self.password,
            )

    def _center_align(self):
        for i in range(1, 10):
            st.write('')
