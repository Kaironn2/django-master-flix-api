from http import HTTPStatus

import requests


def get_nationalities(
    charfield_choices=False,
) -> list[str] | list[tuple[str, str]]:
    url = 'https://restcountries.com/v3.1/all?fields=name'
    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        countries = [country['name']['common'].lower() for country in data]
        countries.sort()

    if charfield_choices:
        countries = tuple((country, country) for country in countries)
    return countries
