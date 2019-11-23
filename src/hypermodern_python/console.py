"""Command-line interface for the hypermodern Python project."""
import asyncio
import urllib.parse

import click
import uvicorn

from . import __version__, splines


def _serve(bind):
    url = urllib.parse.urlsplit(f"//{bind}")
    host = url.hostname or "127.0.0.1"
    port = url.port or 8000
    uvicorn.run("hypermodern_python.app:app", host=host, port=port)


async def _reticulate(count):
    async for spline in splines.reticulate(count):
        click.echo(f"Reticulating spline {spline}...")


@click.command()
@click.option("-n", "--count", default=-1, help="Number of splines to reticulate")
@click.option("--serve", "bind", type=str, help="Run a web server", metavar="HOST:PORT")
@click.version_option(version=__version__)
def main(count: int, bind: str) -> None:
    """The hypermodern Python project."""
    if bind is not None:
        return _serve(bind)

    coroutine = _reticulate(count)
    asyncio.run(coroutine)
