"""Command-line interface for the hypermodern Python project."""
import asyncio
import urllib.parse

import click
import uvicorn

from . import __version__, splines


@click.command()
@click.option("-n", "--count", default=-1, help="Number of splines to reticulate")
@click.option("--serve", type=str, help="Run a web server", metavar="HOST:PORT")
@click.version_option(version=__version__)
def main(count: int, serve: str) -> None:
    """The hypermodern Python project."""
    if serve is not None:
        url = urllib.parse.urlsplit(f"//{serve}")
        host = url.hostname or "127.0.0.1"
        port = url.port or 8000
        return uvicorn.run("hypermodern_python.app:app", host=host, port=port)

    coroutine = splines.reticulate(count)
    for spline in asyncio.run(coroutine):
        click.echo(f"Reticulating spline {spline}...")
