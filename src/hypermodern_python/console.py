"""Command-line interface for the hypermodern Python project."""
import textwrap
from typing import Tuple

import click
import requests

from . import __version__


def random_article() -> Tuple[str, str]:
    """Return a random article from Wikipedia.

    Returns:
        The title and extract of the article

    """
    response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")

    title = response.json()["title"]
    extract = response.json()["extract"]

    return title, extract


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """The hypermodern Python project."""
    title, extract = random_article()

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
