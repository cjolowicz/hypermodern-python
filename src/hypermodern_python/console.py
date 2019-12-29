import textwrap

import click
import requests

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")

    title = response.json()["title"]
    extract = response.json()["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
