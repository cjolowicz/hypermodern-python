from dataclasses import dataclass

import click
import desert
import requests


API_URL: str = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


@dataclass
class Page:
    title: str
    extract: str


schema = desert.schema(Page)


def random_page(language: str = "en") -> Page:
    url = API_URL.format(language=language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            data = response.json()
            return schema.load(data)
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
