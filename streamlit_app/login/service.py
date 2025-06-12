import streamlit as st
from api.service import Auth


def login(username: str, password: str):
    client = Auth()
    response = client.get_token(
        username=username,
        password=password,
    )

    error = response.get('error')
    if error:
        st.error(f'Falha ao realizar login: {error}')
    else:
        st.session_state.token = response.get('access')
        st.rerun()


def logout():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
