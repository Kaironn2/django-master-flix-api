class GenreTexts:
    header = 'Explorar gêneros'
    description = 'Aqui você encontrará uma lista de gêneros de filmes e poderá filtrá-los.'

    error_null_genre = 'Por favor, digite o nome do gênero'
    error_genre_already_exists = 'Gênero já cadastrado no banco de dados.'

    place_holder_genre_register = 'Digite o nome do gênero...'

    warning_inexistent_movie = 'Nenhum filme registrado para esse gênero.'

    @staticmethod
    def sucess_genre_create(genre_name: str) -> str:
        return f'Gênero {genre_name} cadastrado com sucesso!'
