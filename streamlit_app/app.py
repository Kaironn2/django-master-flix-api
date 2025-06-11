import streamlit as st  # noqa: I001

from actors.page import ActorPage
from genres.page import GenrePage
from home.page import HomePage
from movies.page import MoviePage
from login.page import LoginPage
from reviews.page import ReviewPage


class FlixApp:
    def __init__(self):
        pass

    def run(self):
        st.set_page_config(layout='wide', page_title='Flix App')
        if 'token' not in st.session_state:
            self._is_not_authenticated()
        else:
            self._is_authenticated()

    def _is_not_authenticated(self):
        ...

    def _is_authenticated(self):
        self._pages()

        pages_config = []
        for i, page in enumerate(self.pages):
            url_path = page.title.lower().replace(' ', '-')
            pages_config.append(
                st.Page(page.render, title=page.title, default=(i == 0), url_path=url_path)
            )

        pg = st.navigation(pages_config)
        pg.run()

    def _pages(self):
        self.pages = [
            HomePage(),
            MoviePage(),
            ActorPage(),
            GenrePage(),
            ReviewPage(),
        ]


if __name__ == '__main__':
    app = FlixApp()
    app.run()
