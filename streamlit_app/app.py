import streamlit as st  # noqa: I001

from content import home_text


class FlixApp:
    def __init__(self):
        pass

    def _show_home(self):
        st.header(home_text.welcome)
        st.write(home_text.description)

    def _show_genres(self):
        st.header('Explorar Gêneros')
        st.write('Aqui você encontrará uma lista de gêneros de filmes e poderá filtrá-los.')
        generos = ['Ação', 'Comédia', 'Drama', 'Ficção Científica', 'Terror', 'Romance']
        st.markdown('---')
        for genero in generos:
            st.info(f'**{genero}**')

    def _show_actors(self):
        st.header('Perfis de Atores')
        st.write('Pesquise e visualize informações sobre seus atores favoritos.')
        atores = ['Tom Hanks', 'Meryl Streep', 'Denzel Washington', 'Viola Davis']
        st.markdown('---')
        for ator in atores:
            st.success(f'- {ator}')

    def _show_movies(self):
        st.header('Catálogo de Filmes')
        st.write('Navegue por nossa vasta coleção de filmes.')

    def _show_reviews(self):
        st.header('Suas Avaliações')
        st.write('Gerencie e adicione suas avaliações de filmes aqui.')
        pass

    def run(self):
        st.title('Flix App')

        pages_config = [
            st.Page(self._show_home, title='Início'),
            st.Page(self._show_genres, title='Gêneros'),
            st.Page(self._show_actors, title='Atores'),
            st.Page(self._show_movies, title='Filmes'),
            st.Page(self._show_reviews, title='Avaliações'),
        ]

        pg = st.navigation(pages_config)
        pg.run()


if __name__ == '__main__':
    st.set_page_config(layout='wide', page_title='Flix App')
    app = FlixApp()
    app.run()
