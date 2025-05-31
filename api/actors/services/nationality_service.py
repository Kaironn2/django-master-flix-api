from http import HTTPStatus

import requests


def get_nationalities() -> list[str]:
    url = 'https://restcountries.com/v3.1/all?fields=name'
    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        countries = [country['name']['common'] for country in data]
        countries.sort()

    return countries
